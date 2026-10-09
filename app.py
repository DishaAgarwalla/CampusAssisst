# ==================================================
# CampusAssist — College Helpdesk Chatbot — Flask Backend
# ==================================================
# NOTE: All intent / topic / scoring logic is
# UNCHANGED. Only structure, safety & polish added.
# ==================================================

from flask import Flask, jsonify, request, render_template
import json
import re
import os
import logging

# --------------------------------------------------
# Logging configuration
# --------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s — %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)


# --------------------------------------------------
# Application factory setup
# --------------------------------------------------
app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False


# ==================================================
# Load College Data (safe)
# ==================================================
DATA_FILE = os.path.join(os.path.dirname(__file__), "college_data.json")

try:
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        college_data = json.load(file)
    logger.info("College data loaded successfully (%d categories).", len(college_data))
except FileNotFoundError:
    logger.error("college_data.json not found — starting with empty data.")
    college_data = {}
except json.JSONDecodeError as e:
    logger.error("college_data.json is corrupted: %s", e)
    college_data = {}


# ==================================================
# Home Page
# ==================================================
@app.route("/")
def home():
    return render_template("index.html")


# ==================================================
# Health Check (useful for demo / deployment)
# ==================================================
@app.route("/health")
def health():
    return jsonify({
        "status": "ok",
        "categories": list(college_data.keys()),
    })


# ==================================================
# Text Normalization
# ==================================================
def normalize_text(text):
    """
    Convert text into a clean and normalized form.
    """
    text = text.lower().strip()
    text = re.sub(r"[^\w\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text


# ==================================================
# Calculate Intent Score
# ==================================================
def calculate_score(message, keywords):
    """
    Calculate how strongly the message matches an intent.
    Multi-word phrases receive a higher score.
    """
    score = 0

    for keyword in keywords:
        keyword = keyword.lower()

        if " " in keyword:
            if keyword in message:
                score += 4
        else:
            pattern = r"\b" + re.escape(keyword) + r"\b"
            if re.search(pattern, message):
                score += 1

    return score


# ==================================================
# Detect Main Intent
# ==================================================
def detect_intent(message):

    intents = {
        "admissions": [
            "admission process", "admission procedure", "how to apply",
            "documents for admission", "admission documents",
            "admission", "admissions", "apply", "application", "applications",
            "eligibility", "eligible", "enrollment", "enrolment"
        ],
        "departments": [
            "engineering branches", "engineering branch", "field of study",
            "departments available", "branches available", "streams available",
            "department", "departments", "branch", "branches", "stream", "streams"
        ],
        "timetable": [
            "class schedule", "schedule of classes", "class timing",
            "class timings", "lecture schedule", "lecture timing",
            "lecture timings", "time table", "timetable",
            "class time", "class times"
        ],
        "examination": [
            "exam schedule", "examination schedule", "exam date", "exam dates",
            "exam timing", "exam timings", "when are the exams",
            "when will the exams", "exam", "exams", "examination",
            "examinations", "test", "tests"
        ],
        "attendance": [
            "attendance percentage", "attendance requirement",
            "minimum attendance", "attendance", "attend",
            "absent", "absence", "presence"
        ],
        "courses": [
            "academic program", "academic programs", "course structure",
            "course details", "subject details", "course", "courses",
            "subject", "subjects", "curriculum", "syllabus", "degree"
        ],
        "faculty": [
            "teaching staff", "faculty members", "faculty details",
            "professor", "professors", "teacher", "teachers",
            "faculty", "lecturer", "lecturers", "staff"
        ],
        "facilities": [
            "campus facilities", "campus facility", "computer lab",
            "computer labs", "laboratory", "laboratories", "facility",
            "facilities", "library", "libraries", "lab", "labs",
            "campus", "classroom", "classrooms", "sports", "canteen"
        ],
        "placement": [
            "campus recruitment", "campus recruitment drive",
            "campus recruitment drives", "placement opportunities",
            "placement opportunity", "placement drive", "placement drives",
            "job opportunity", "job opportunities", "career opportunity",
            "career opportunities", "recruitment drive", "recruitment drives",
            "recruitment", "placement", "placements", "job", "jobs",
            "career", "careers", "company", "companies", "interview", "interviews"
        ],
        "scholarships": [
            "financial assistance", "financial aid", "financial support",
            "student aid", "education funding", "scholarship eligibility",
            "scholarship application", "scholarship", "scholarships"
        ]
    }

    strong_intents = {
        "scholarships": [
            "scholarship", "scholarships", "financial assistance",
            "financial aid", "financial support", "student aid", "education funding"
        ],
        "placement": [
            "placement", "placements", "campus recruitment",
            "recruitment drive", "placement training", "placement opportunities"
        ],
        "admissions": [
            "admission", "admissions", "admission process",
            "admission procedure", "admission documents"
        ],
        "attendance": [
            "attendance", "minimum attendance",
            "attendance percentage", "attendance requirement"
        ],
        "timetable": [
            "timetable", "time table", "class schedule", "lecture schedule"
        ],
        "examination": [
            "exam", "exams", "examination",
            "examination schedule", "exam schedule"
        ],
        "departments": [
            "department", "departments",
            "engineering branch", "engineering branches"
        ],
        "courses": ["course", "courses", "syllabus", "curriculum"],
        "faculty": [
            "faculty", "faculty members", "professor",
            "professors", "teacher", "teachers"
        ],
        "facilities": [
            "campus facilities", "computer lab", "computer labs",
            "library", "laboratory", "laboratories"
        ]
    }

    strong_matches = []

    for intent, keywords in strong_intents.items():
        for keyword in keywords:
            if " " in keyword:
                if keyword in message:
                    strong_matches.append(intent)
            else:
                pattern = r"\b" + re.escape(keyword) + r"\b"
                if re.search(pattern, message):
                    strong_matches.append(intent)

    if strong_matches:
        unique_matches = list(dict.fromkeys(strong_matches))
        return unique_matches[0]

    scores = {intent: calculate_score(message, keywords)
              for intent, keywords in intents.items()}

    best_intent = max(scores, key=scores.get)
    best_score = scores[best_intent]

    if best_score == 0:
        return None

    return best_intent


# ==================================================
# Detect Specific Topic
# ==================================================
def detect_topic(message, intent):

    topic_keywords = {
        "admissions": {
            "documents": ["document", "documents", "certificate", "certificates",
                          "paper", "papers", "what do i need"],
            "eligibility": ["eligibility", "eligible", "qualification",
                            "qualify", "requirements"],
            "procedure": ["procedure", "process", "how to apply",
                          "how can i apply", "steps"],
            "application": ["application", "apply", "application form"]
        },
        "departments": {
            "branches": ["branch", "branches", "engineering branch",
                         "engineering branches"],
            "streams": ["stream", "streams"],
            "fields": ["field", "fields", "field of study"]
        },
        "timetable": {
            "schedule": ["schedule", "class schedule", "timetable", "time table"],
            "timings": ["timing", "timings", "class time", "class times",
                        "lecture time", "lecture timing"],
            "changes": ["change", "changes", "changed", "updated"],
            "location": ["where", "find", "located"]
        },
        "examination": {
            "schedule": ["schedule", "exam schedule", "examination schedule", "timetable"],
            "dates": ["date", "dates", "when", "when are"],
            "timings": ["timing", "timings", "time"],
            "documents": ["document", "documents", "identity card", "id card", "id"],
            "instructions": ["instruction", "instructions", "rules",
                             "what should i bring"]
        },
        "attendance": {
            "requirement": ["requirement", "minimum", "percentage",
                            "how much attendance"],
            "recording": ["record", "recorded", "recording", "maintained"],
            "checking": ["check", "checking", "where can i check",
                         "see my attendance"],
            "absence": ["absent", "absence", "leave"]
        },
        "courses": {
            "subjects": ["subject", "subjects"],
            "structure": ["structure", "course structure"],
            "syllabus": ["syllabus", "curriculum"],
            "degree": ["degree", "program", "programs"]
        },
        "faculty": {
            "teaching": ["teach", "teaching", "teacher", "teachers"],
            "contact": ["contact", "email", "phone", "reach"],
            "department": ["department", "which department"],
            "information": ["information", "details", "faculty details"]
        },
        "facilities": {
            "library": ["library", "libraries", "books"],
            "computer_labs": ["computer lab", "computer labs", "computer laboratory"],
            "laboratories": ["laboratory", "laboratories", "lab", "labs"],
            "classrooms": ["classroom", "classrooms"],
            "sports": ["sports", "sport", "recreation", "recreational"],
            "canteen": ["canteen", "food", "cafeteria"]
        },
        "placement": {
            "recruitment": ["recruitment", "recruitment drive",
                            "recruitment drives", "campus recruitment",
                            "campus recruitment drive", "campus recruitment drives"],
            "training": ["training", "placement training", "aptitude training",
                         "interview preparation", "communication training"],
            "opportunities": ["opportunity", "opportunities",
                              "placement opportunity", "placement opportunities",
                              "job opportunity", "job opportunities",
                              "career opportunity", "career opportunities"],
            "companies": ["company", "companies", "which companies"],
            "eligibility": ["eligibility", "eligible", "criteria", "requirements"],
            "interviews": ["interview", "interviews", "technical interview",
                           "aptitude test", "recruitment round"]
        },
        "scholarships": {
            "eligibility": ["eligibility", "eligible", "who can apply", "qualification"],
            "application": ["application", "apply", "how can i apply",
                            "application process"],
            "documents": ["document", "documents", "certificate",
                          "certificates", "what do i need"],
            "financial_assistance": ["financial assistance", "financial aid",
                                     "financial support", "student aid"],
            "deadlines": ["deadline", "deadlines", "last date", "due date"]
        }
    }

    topics = topic_keywords.get(intent, {})
    best_topic = None
    best_score = 0

    for topic, keywords in topics.items():
        score = calculate_score(message, keywords)
        if score > best_score:
            best_score = score
            best_topic = topic

    return best_topic or "general"


# ==================================================
# Suggested Questions
# ==================================================
suggestions = {
    "admissions": [
        "What documents are required for admission?",
        "What are the eligibility requirements?",
        "How can I apply for admission?"
    ],
    "departments": [
        "What departments are available?",
        "Which engineering branches are available?",
        "What fields of study are offered?"
    ],
    "timetable": [
        "Where can I find the timetable?",
        "When are classes conducted?",
        "Can the timetable change?"
    ],
    "examination": [
        "Where can I find the exam schedule?",
        "What should I bring to the exam?",
        "Who publishes the exam timetable?"
    ],
    "attendance": [
        "What is the attendance requirement?",
        "How is attendance recorded?",
        "Where can I check my attendance?"
    ],
    "courses": [
        "What subjects are available?",
        "Where can I find the syllabus?",
        "What is included in the course structure?"
    ],
    "faculty": [
        "Who are the teaching staff?",
        "How can I contact the faculty?",
        "Which department does a professor belong to?"
    ],
    "facilities": [
        "Does the college have a library?",
        "Are computer labs available?",
        "What facilities are available on campus?"
    ],
    "placement": [
        "Are there campus recruitment drives?",
        "What placement training is provided?",
        "What are the placement opportunities?"
    ],
    "scholarships": [
        "Who can apply for scholarships?",
        "What documents are required?",
        "How can I apply for financial assistance?"
    ]
}


# ==================================================
# Chat Endpoint
# ==================================================
@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json(silent=True)

    if not data:
        return jsonify({
            "response": ["I couldn't understand your request."],
            "intent": None, "topic": None, "suggestions": []
        }), 400

    original_message = str(data.get("message", "")).strip()

    if not original_message:
        return jsonify({
            "response": ["Please type a question."],
            "intent": None, "topic": None, "suggestions": []
        })

    message = normalize_text(original_message)

    # ---------------- Greetings ----------------
    if message in ["hi", "hii", "hiii", "hello", "hey",
                   "good morning", "good afternoon", "good evening"]:
        return jsonify({
            "response": ["Hello! 👋 I'm CampusAssist, your College "
                         "Helpdesk Assistant. How can I help you today?"],
            "intent": "greeting", "topic": None,
            "suggestions": [
                "What departments are available?",
                "What courses are available?",
                "When are the exams?"
            ]
        })

    # ---------------- Thank You ----------------
    if message in ["thanks", "thank you", "thank",
                   "thanks a lot", "thank you so much"]:
        return jsonify({
            "response": ["You're welcome! 😊 Feel free to ask me another "
                         "college-related question."],
            "intent": "thank_you", "topic": None,
            "suggestions": [
                "What departments are available?",
                "What scholarships are available?",
                "What are the placement opportunities?"
            ]
        })

    # ---------------- Help ----------------
    if message in ["help", "what can you do",
                   "how can you help", "what do you know"]:
        return jsonify({
            "response": ["I can help you with Admissions, Departments, "
                         "Timetable, Examinations, Attendance, Courses, "
                         "Faculty, Campus Facilities, Placements and "
                         "Scholarships."],
            "intent": "help", "topic": None,
            "suggestions": [
                "What are the admission requirements?",
                "What departments are available?",
                "What are the placement opportunities?"
            ]
        })

    # ---------------- Intent ----------------
    intent = detect_intent(message)

    if intent is None:
        return jsonify({
            "response": ["I don't have that information."],
            "intent": "unknown", "topic": None,
            "suggestions": [
                "What departments are available?",
                "What courses are available?",
                "What are the admission requirements?"
            ]
        })

    topic = detect_topic(message, intent)

    information = college_data.get(intent, {}).get("information", {})

    response = information.get(topic)
    if response is None:
        response = information.get("general",
                                   "I don't have that information.")

    logger.info("intent=%s topic=%s query=%r", intent, topic, original_message)

    return jsonify({
        "response": [response],
        "intent": intent,
        "topic": topic,
        "suggestions": suggestions.get(intent, [])
    })


# ==================================================
# Start Flask Server
# ==================================================
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)