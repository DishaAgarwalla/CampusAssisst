# 🎓 CampusAssisst — AI College Helpdesk Chatbot

<p align="center">
  <strong>A Simple, Interactive College Helpdesk Chatbot Built with Python and Flask</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Flask-Web%20Framework-black?logo=flask" alt="Flask">
  <img src="https://img.shields.io/badge/HTML5-Frontend-orange?logo=html5" alt="HTML5">
  <img src="https://img.shields.io/badge/CSS3-Styling-blue?logo=css3" alt="CSS3">
  <img src="https://img.shields.io/badge/JavaScript-Interactive-yellow?logo=javascript" alt="JavaScript">
  <img src="https://img.shields.io/badge/Status-Completed-success" alt="Project Status">
</p>

## 📌 About the Project

**CampusAssisst** is a lightweight, web-based college helpdesk chatbot designed to answer common student queries through a simple and interactive chat interface.

Students can ask questions about admissions, departments, timetables, examinations, attendance, courses, faculty, campus facilities, placements, and scholarships. The chatbot processes questions using predefined intent-matching logic and retrieves relevant information from a JSON-based knowledge base.

The project uses Python and Flask for backend processing, along with HTML, CSS, and JavaScript for the frontend. It is designed as a beginner-friendly academic project that demonstrates the fundamentals of chatbot development and web application integration without requiring paid APIs or external AI services.

## 🎯 Objectives

* Provide quick answers to frequently asked college-related questions.
* Create a simple and user-friendly chatbot interface.
* Organize college information in a structured JSON file.
* Use Python and Flask to handle user queries and generate responses.
* Demonstrate communication between frontend and backend components.
* Avoid paid API subscriptions and external AI service dependencies.
* Provide a clear fallback response when the requested information is unavailable.

## ✨ Features

* **Interactive Chat Interface:** Students can ask questions through a conversational interface.
* **Multiple Query Categories:** Covers admissions, departments, timetables, examinations, attendance, courses, faculty, facilities, placements, and scholarships.
* **Intent Detection:** Uses keyword and phrase matching to identify the likely topic of a question.
* **JSON-Based Knowledge Base:** Stores college-related information in `college_data.json`.
* **Fallback Responses:** Returns `I don't have that information.` when the chatbot cannot provide a supported answer.
* **Conversation History:** Displays messages during the current chat session.
* **Message Timestamps:** Shows the time associated with chat messages.
* **Suggested Questions:** Offers example questions to help students explore available information.
* **Formatted Responses:** Displays answers in a readable format, including lists where appropriate.
* **No Paid API Required:** Runs using local application logic and predefined data.
* **Lightweight Setup:** Suitable for development and demonstration in Visual Studio Code.

## 🛠️ Technology Stack

| Technology         | Purpose                                      |
| ------------------ | -------------------------------------------- |
| Python             | Backend programming and chatbot logic        |
| Flask              | Web server and HTTP request handling         |
| HTML5              | Structure of the chatbot interface           |
| CSS3               | Layout, styling, and responsive presentation |
| JavaScript         | Chat interactions and frontend behavior      |
| JSON               | Storage of predefined college information    |
| Git and GitHub     | Version control and project hosting          |
| Visual Studio Code | Development environment                      |

## 🧠 How It Works

1. The student enters a question in the chatbot interface.
2. JavaScript sends the question to the Flask backend.
3. The backend normalizes the text and checks for relevant keywords and phrases.
4. The chatbot identifies the most likely intent or topic.
5. The application retrieves a suitable response from its predefined logic and JSON knowledge base.
6. Flask returns the response to the frontend.
7. JavaScript displays the answer in the chat interface, along with the available message details and suggested questions.

If the chatbot cannot identify a suitable answer, it returns a predefined fallback message rather than inventing college information.

**Note:** CampusAssisst is a rule-based chatbot, not a generative AI or large language model application. Its responses depend on the implemented rules and available data.

## 📚 Supported Query Categories

| Category          | Example Question                            |
| ----------------- | ------------------------------------------- |
| Admissions        | How can I apply for admission?              |
| Departments       | Which departments are available?            |
| Timetable         | When will the timetable be announced?       |
| Examination       | When are the examinations?                  |
| Attendance        | Where can I get attendance information?     |
| Courses           | What courses are available?                 |
| Faculty           | How can I contact the faculty?              |
| Campus Facilities | What facilities are available on campus?    |
| Placement         | What placement opportunities are available? |
| Scholarships      | What scholarship information is available?  |

*The actual answers depend on the data and rules implemented in the project.*

## 📂 Project Structure

```text
CampusAssisst/
│
├── app.py                  # Flask application and chatbot logic
├── college_data.json       # College information and response data
├── requirements.txt        # Python dependencies
├── .gitignore              # Files excluded from Git
├── README.md               # Project documentation
│
├── templates/
│   └── index.html          # Chatbot webpage
│
├── static/
│   ├── css/
│   │   └── style.css       # Chatbot styling
│   │
│   └── js/
│       └── script.js       # Frontend interaction logic
│
└── venv/                   # Local virtual environment (not uploaded)
```

## ⚙️ Installation and Setup

### Prerequisites

Before running the project, ensure you have installed:

* Python 3.10 or a compatible version
* Visual Studio Code
* Git (optional, for cloning the repository)
* A modern web browser

### 1. Clone the Repository

```bash
git clone https://github.com/DishaAgarwalla/CampusAssisst.git
```

### 2. Navigate to the Project Folder

```bash
cd CampusAssisst
```

### 3. Create a Virtual Environment

**Windows PowerShell:**

```powershell
python -m venv venv
```

### 4. Activate the Virtual Environment

```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks script execution, you can use Command Prompt instead:

```bat
venv\Scripts\activate.bat
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Application

```bash
python app.py
```

### 7. Open the Chatbot

Open your browser and visit the local address printed by Flask in the terminal. If the application uses Flask's default development settings, this is usually:

```text
http://127.0.0.1:5000/
```

You can now start asking questions through the CampusAssisst chat interface.

## 💬 Example Interaction

**Student:** Which departments are available?

**CampusAssisst:** Lists the departments configured in the application's knowledge base.

**Student:** What facilities are available on campus?

**CampusAssisst:** Provides the campus facility information configured in the project.

**Student:** What is the hostel fee?

**CampusAssisst:** I don't have that information.

*These examples illustrate the intended behavior. Responses depend on the current application data and implementation.*

## 🔧 Customization

You can customize CampusAssisst by editing the following files:

* **`college_data.json`** — Add, update, or remove college information.
* **`app.py`** — Modify intent detection, response handling, and backend logic.
* **`templates/index.html`** — Update the structure of the chat interface.
* **`static/css/style.css`** — Change colors, spacing, typography, and layout.
* **`static/js/script.js`** — Improve chat interactions, timestamps, suggestions, and message rendering.
* **`requirements.txt`** — Maintain the Python packages required to run the application.

To provide reliable answers, keep the knowledge base accurate and ensure the chatbot rules cover the questions you want to support.

## 🔐 Privacy and API Requirements

* No paid OpenAI API key is required.
* No Ollama installation is required.
* The chatbot uses its own predefined logic and local JSON data.
* The application is intended for local academic demonstration unless separately configured for deployment.
* Do not add real student records, passwords, or other sensitive information to the repository.

## 🚧 Limitations

* The chatbot does not generate answers using a large language model.
* It may not understand questions phrased in unexpected ways.
* Its responses are limited to implemented rules and available college information.
* It does not automatically retrieve live college notices, timetables, attendance records, or placement updates.
* The accuracy of responses depends on the completeness of the knowledge base.
* Conversation history is not necessarily persistent across browser sessions.

## 🚀 Future Enhancements

Potential improvements include:

* Expanding the knowledge base with verified college information.
* Improving intent matching and handling of alternative question phrasings.
* Adding an administrator interface for updating college data.
* Integrating a college notice or timetable management system.
* Adding persistent chat history if required.
* Supporting multiple languages.
* Deploying the application so students can access it online.

## 🎓 Learning Outcomes

This project provides practical experience with:

* Python application development.
* Flask routes and HTTP request-response handling.
* Frontend and backend integration.
* JavaScript-based chat interfaces.
* JSON data management.
* Basic intent detection and text processing.
* Git, GitHub, and project documentation.
* Error handling and fallback responses.

## 👩‍💻 Author

**Disha Agarwalla**

* GitHub: [@DishaAgarwalla](https://github.com/DishaAgarwalla)
* LinkedIn: [Disha Agarwalla](https://www.linkedin.com/in/disha-agarwalla-10884b31b/)

## 📄 License

This project is intended for educational and academic purposes. A formal open-source license can be added to the repository if you choose to distribute the project under specific reuse terms.

---

<p align="center">
  <strong>CampusAssisst — Making College Information Easier to Access.</strong>
</p>
