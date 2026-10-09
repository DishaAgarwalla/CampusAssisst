# 🎓 CampusAssisst — AI College Helpdesk Chatbot

<p align="center">
  <strong>An Interactive AI-Powered College Helpdesk Chatbot Built with Python, Flask, and the ChatGPT API</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Flask-Web%20Framework-black?logo=flask" alt="Flask">
  <img src="https://img.shields.io/badge/OpenAI-ChatGPT%20API-412991?logo=openai" alt="OpenAI">
  <img src="https://img.shields.io/badge/HTML5-Frontend-orange?logo=html5" alt="HTML5">
  <img src="https://img.shields.io/badge/CSS3-Styling-blue?logo=css3" alt="CSS3">
  <img src="https://img.shields.io/badge/JavaScript-Interactive-yellow?logo=javascript" alt="JavaScript">
</p>

## 📌 About the Project

**CampusAssisst** is a web-based AI college helpdesk chatbot designed to help students get answers to common college-related questions through a simple and interactive chat interface.

Students can ask questions about admissions, departments, timetables, examinations, attendance, courses, faculty, campus facilities, placements, and scholarships. The chatbot uses the **ChatGPT API** to understand questions written in natural language and generate relevant, conversational responses.

The project uses Python and Flask for backend processing, HTML, CSS, and JavaScript for the frontend, and the OpenAI API to power its conversational capabilities. It aims to make college information easier to access through an AI-powered assistant.

## 🎯 Objectives

* Provide quick and conversational answers to college-related questions.
* Develop an interactive and user-friendly chatbot interface.
* Use the ChatGPT API to understand and respond to natural-language questions.
* Integrate an AI service with a Python Flask web application.
* Connect frontend interactions with backend API processing.
* Handle questions for which reliable information is unavailable.
* Demonstrate the practical application of AI in a college helpdesk system.

## ✨ Features

* **AI-Powered Conversations:** Uses the ChatGPT API to generate natural-language responses.
* **Multiple Query Categories:** Supports questions about admissions, departments, timetables, examinations, attendance, courses, faculty, campus facilities, placements, and scholarships.
* **Natural-Language Understanding:** Allows students to ask questions in their own words.
* **Interactive Chat Interface:** Provides a conversational interface for sending questions and receiving answers.
* **Conversation History:** Displays messages exchanged during the current chat session.
* **Message Timestamps:** Shows the time associated with chat messages.
* **Suggested Questions:** Helps students discover topics they can ask about.
* **Formatted Responses:** Presents answers in a readable format, including lists where appropriate.
* **Fallback Handling:** Provides an appropriate response when the chatbot cannot answer a question reliably.
* **Modular Architecture:** Separates backend logic, frontend presentation, and chatbot interactions.
* **Secure API Configuration:** Supports storing the API key in an environment variable instead of exposing it in source code.

## 🛠️ Technology Stack

| Technology         | Purpose                                                   |
| ------------------ | --------------------------------------------------------- |
| Python             | Backend programming and application logic                 |
| Flask              | Web server and HTTP request handling                      |
| OpenAI ChatGPT API | Natural-language understanding and AI-generated responses |
| HTML5              | Structure of the chatbot interface                        |
| CSS3               | Styling and responsive presentation                       |
| JavaScript         | Chat interactions and frontend behavior                   |
| JSON               | Structured data storage, if required by the application   |
| Git and GitHub     | Version control and project hosting                       |
| Visual Studio Code | Development environment                                   |

## 🧠 How It Works

1. The student enters a question in the chatbot interface.
2. JavaScript sends the question to the Flask backend.
3. The backend receives and processes the request.
4. Flask sends the question to the ChatGPT API using the configured model and API credentials.
5. The AI generates a response based on the question and the instructions provided to it.
6. The backend returns the response to the frontend.
7. JavaScript displays the answer in the chat interface, along with relevant message details and suggested questions where supported.

The chatbot can be configured to focus on college-related questions and respond appropriately when information is unavailable. For institution-specific accuracy, verified college information should be supplied to the application or made accessible to the AI through an appropriate data source.

## 📂 Project Structure

```text
CampusAssisst/
│
├── app.py                  # Flask application and AI integration
├── college_data.json       # College-related data, if used
├── requirements.txt        # Python dependencies
├── .gitignore              # Files excluded from Git
├── README.md               # Project documentation
├── .env                    # API key and environment variables (not uploaded)
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
└── venv/                   # Local Python virtual environment (not uploaded)
```

*Note: `.env` is only needed if the application uses environment variables for configuration. It and `venv/` should be excluded from Git using `.gitignore`.*

## ⚙️ Installation and Setup

### Prerequisites

Before running the project, ensure you have installed:

* Python 3.10 or a compatible version
* Visual Studio Code
* Git (optional, for cloning the repository)
* A modern web browser
* An OpenAI API key with API access and available billing or credits as required

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

Ensure that `requirements.txt` includes the packages required by your application, such as Flask, the OpenAI Python SDK, and `python-dotenv` if you use a `.env` file.

If the required packages are not already listed, install them with:

```bash
pip install flask openai python-dotenv
```

### 6. Configure the OpenAI API Key

Create a `.env` file in the project root directory and add your API key:

```env
OPENAI_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your own API key.

**Important:** Never upload your API key to GitHub or place it directly in frontend JavaScript. Keep `.env` in `.gitignore` and make API requests from the backend.

The ChatGPT API is billed separately from a ChatGPT subscription. API access may require billing or available credits; do not assume that API usage is free.

### 7. Run the Application

```bash
python app.py
```

### 8. Open the Chatbot

Open your browser and visit the local address printed by Flask in the terminal. If the application uses Flask's default development settings, this is usually:

```text
http://127.0.0.1:5000/
```

You can now start asking questions through the CampusAssisst chat interface.

## 💬 Example Interaction

**Student:** What departments are available in a college?

**CampusAssisst:** The AI generates a conversational answer based on the context available to it.

**Student:** How can I find out about scholarships?

**CampusAssisst:** The AI can explain general scholarship options and provide relevant guidance. For accurate information about a particular college's scholarships, the application should provide verified institutional details.

*Example responses depend on the API integration, model configuration, and instructions implemented in the application.*


## 🎓 Learning Outcomes

This project provides practical experience with:

* Python application development.
* Flask routes and HTTP request-response handling.
* OpenAI API integration.
* Natural-language chatbot development.
* Frontend and backend integration.
* JavaScript-based chat interfaces.
* Environment variables and API key security.
* JSON data management.
* Git, GitHub, and project documentation.
* Error handling and external API communication.


## 📄 License

This project is intended for educational and academic purposes. A formal open-source license can be added to the repository if you choose to distribute the project under specific reuse terms.

---

<p align="center">
  <strong>CampusAssisst — Making College Information Easier to Access with AI.</strong>
</p>
