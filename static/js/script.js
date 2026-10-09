// ==================================================
// CampusAssist — College Helpdesk Chatbot — Frontend
// ==================================================
// NOTE: Core logic (send, restore, suggestions,
// history, intent handling) is UNCHANGED.
// Only polish, safety & UX features added.
// ==================================================


// ==================================================
// Global Variables
// ==================================================
let chatBox;
let input;
let sendBtn;
let chatHistory = [];
let isSending = false;


// ==================================================
// Initialize Application
// ==================================================
document.addEventListener("DOMContentLoaded", function () {

    chatBox = document.getElementById("chat-box");
    input   = document.getElementById("user-input");
    sendBtn = document.getElementById("send-btn");

    if (!chatBox || !input) {
        console.error("Chatbot elements were not found.");
        return;
    }

    // ---- Load saved conversation ----
    try {
        chatHistory = JSON.parse(localStorage.getItem("collegeChatHistory")) || [];
    } catch (error) {
        console.error("Could not load chat history:", error);
        chatHistory = [];
    }

    // ---- Restore theme ----
    if (localStorage.getItem("collegeChatTheme") === "dark") {
        document.body.classList.add("dark");
        document.getElementById("theme-toggle").textContent = "☀️";
    }

    // ---- Restore conversation ----
    restoreChatHistory();

    // ---- Enter key ----
    input.addEventListener("keydown", function (event) {
        if (event.key === "Enter" && !event.shiftKey) {
            event.preventDefault();
            sendMessage();
        }
    });

    // ---- Send button ----
    if (sendBtn) sendBtn.addEventListener("click", () => sendMessage());

    // ---- Header actions ----
    document.getElementById("theme-toggle").addEventListener("click", toggleTheme);
    document.getElementById("clear-chat").addEventListener("click", clearChat);
    document.getElementById("export-chat").addEventListener("click", exportChat);

    // ---- Enable / disable send button ----
    input.addEventListener("input", updateSendButton);
    updateSendButton();

    // ---- Focus input ----
    input.focus();
});


// ==================================================
// UI Helpers
// ==================================================

function updateSendButton() {
    if (!sendBtn) return;
    sendBtn.disabled = input.value.trim() === "" || isSending;
}

function toggleTheme() {
    document.body.classList.toggle("dark");
    const isDark = document.body.classList.contains("dark");
    localStorage.setItem("collegeChatTheme", isDark ? "dark" : "light");
    document.getElementById("theme-toggle").textContent = isDark ? "☀️" : "🌙";
}

function clearChat() {
    if (!confirm("Clear the entire conversation?")) return;
    chatHistory = [];
    saveChatHistory();
    chatBox.innerHTML = "";

    // Re-inject the welcome message
    const wrapper = document.createElement("div");
    wrapper.className = "message-container bot-container";
    wrapper.innerHTML = `
        <div class="avatar bot-avatar" aria-hidden="true">🎓</div>
        <div class="message-content">
            <div class="message bot-message">
                <p>Hello! 👋 I'm CampusAssist, your College Helpdesk Assistant. How can I help you today?</p>
            </div>
            <div class="message-time">Just now</div>
        </div>`;
    chatBox.appendChild(wrapper);
}

function exportChat() {
    if (chatHistory.length === 0) {
        alert("Nothing to export yet.");
        return;
    }

    const lines = chatHistory.map(item => {
        const who = item.sender === "user" ? "Student" : "CampusAssist";
        const text = item.sender === "user" ? item.text : (item.response || []).join(" ");
        return `[${item.timestamp}] ${who}: ${text}`;
    });

    const blob = new Blob([lines.join("\n")], { type: "text/plain" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "campusassist-chat.txt";
    a.click();
    URL.revokeObjectURL(url);
}


// ==================================================
// Save Chat History
// ==================================================
function saveChatHistory() {
    try {
        localStorage.setItem("collegeChatHistory", JSON.stringify(chatHistory));
    } catch (error) {
        console.error("Could not save chat history:", error);
    }
}


// ==================================================
// Get Current Time
// ==================================================
function getCurrentTime() {
    return new Date().toLocaleTimeString([], {
        hour: "2-digit",
        minute: "2-digit"
    });
}


// ==================================================
// Normalize Question
// ==================================================
function normalizeQuestion(text) {
    return String(text)
        .toLowerCase()
        .replace(/[^\w\s]/g, "")
        .replace(/\s+/g, " ")
        .trim();
}


// ==================================================
// Remove Existing Suggestions
// ==================================================
function removeSuggestions() {
    chatBox.querySelectorAll(".suggestions").forEach(el => el.remove());
}


// ==================================================
// Typing Indicator
// ==================================================
function showTypingIndicator() {
    const container = document.createElement("div");
    container.className = "message-container bot-container";
    container.id = "typing-indicator";

    const avatar = document.createElement("div");
    avatar.className = "avatar bot-avatar";
    avatar.textContent = "🎓";

    const bubble = document.createElement("div");
    bubble.className = "typing-indicator";
    bubble.innerHTML = "<span></span><span></span><span></span>";

    container.appendChild(avatar);
    container.appendChild(bubble);
    chatBox.appendChild(container);
    scrollToBottom();
}

function hideTypingIndicator() {
    const el = document.getElementById("typing-indicator");
    if (el) el.remove();
}


// ==================================================
// Add User Message
// ==================================================
function addUserMessage(message, timestamp) {
    const container = document.createElement("div");
    container.className = "message-container user-container";

    const avatar = document.createElement("div");
    avatar.className = "avatar user-avatar";
    avatar.textContent = "🧑";

    const content = document.createElement("div");
    content.className = "message-content";

    const bubble = document.createElement("div");
    bubble.className = "message user-message";
    bubble.textContent = message;

    const time = document.createElement("div");
    time.className = "message-time";
    time.textContent = timestamp;

    content.appendChild(bubble);
    content.appendChild(time);
    container.appendChild(avatar);
    container.appendChild(content);

    chatBox.appendChild(container);
    scrollToBottom();
}


// ==================================================
// Add Bot Message
// ==================================================
function addBotMessage(response, timestamp) {
    const container = document.createElement("div");
    container.className = "message-container bot-container";

    const avatar = document.createElement("div");
    avatar.className = "avatar bot-avatar";
    avatar.textContent = "🎓";

    const content = document.createElement("div");
    content.className = "message-content";

    const bubble = document.createElement("div");
    bubble.className = "message bot-message";

    let messages = response;
    if (!Array.isArray(messages)) {
        messages = [String(messages)];
    }

    messages.forEach(function (text) {
        const paragraph = document.createElement("p");
        paragraph.textContent = "• " + text;
        bubble.appendChild(paragraph);
    });

    const time = document.createElement("div");
    time.className = "message-time";
    time.textContent = timestamp;

    content.appendChild(bubble);
    content.appendChild(time);
    container.appendChild(avatar);
    container.appendChild(content);

    chatBox.appendChild(container);
    scrollToBottom();
}


// ==================================================
// Add Suggested Questions
// ==================================================
function addSuggestions(suggestions, currentQuestion = "") {

    removeSuggestions();

    if (!Array.isArray(suggestions) || suggestions.length === 0) {
        return;
    }

    const normalizedCurrentQuestion = normalizeQuestion(currentQuestion);

    const filteredSuggestions = suggestions.filter(
        s => normalizeQuestion(s) !== normalizedCurrentQuestion
    );

    const uniqueSuggestions = [
        ...new Set(filteredSuggestions.map(s => String(s).trim()))
    ];

    if (uniqueSuggestions.length === 0) return;

    const container = document.createElement("div");
    container.className = "suggestions";

    const title = document.createElement("div");
    title.className = "suggestions-title";
    title.textContent = "💡 You can also ask";
    container.appendChild(title);

    uniqueSuggestions.forEach(function (suggestion) {
        const button = document.createElement("button");
        button.type = "button";
        button.className = "suggestion-button";
        button.textContent = suggestion;

        button.addEventListener("click", function (event) {
            event.preventDefault();
            event.stopPropagation();
            if (isSending) return;
            sendMessage(suggestion);
        });

        container.appendChild(button);
    });

    chatBox.appendChild(container);
    scrollToBottom();
}


// ==================================================
// Scroll Chat to Bottom
// ==================================================
function scrollToBottom() {
    if (!chatBox) return;
    setTimeout(() => {
        chatBox.scrollTop = chatBox.scrollHeight;
    }, 50);
}


// ==================================================
// Restore Chat History
// ==================================================
function restoreChatHistory() {

    if (!Array.isArray(chatHistory) || chatHistory.length === 0) {
        return;
    }

    chatBox.innerHTML = "";

    chatHistory.forEach(function (chat) {
        if (chat.sender === "user") {
            addUserMessage(chat.text, chat.timestamp);
        } else if (chat.sender === "bot") {
            addBotMessage(chat.response, chat.timestamp);
        }
    });

    const botMessages = chatHistory.filter(
        chat => chat.sender === "bot"
            && Array.isArray(chat.suggestions)
            && chat.suggestions.length > 0
    );

    if (botMessages.length > 0) {
        addSuggestions(botMessages[botMessages.length - 1].suggestions);
    }
}


// ==================================================
// Send Message
// ==================================================
async function sendMessage(suggestionMessage = null) {

    let message;
    if (typeof suggestionMessage === "string" && suggestionMessage.trim() !== "") {
        message = suggestionMessage.trim();
    } else {
        message = input.value.trim();
    }

    if (message === "") return;
    if (isSending) return;

    isSending = true;
    updateSendButton();

    removeSuggestions();

    // ---- Display user message ----
    const userTimestamp = getCurrentTime();
    addUserMessage(message, userTimestamp);

    // ---- Save user message ----
    chatHistory.push({
        sender: "user",
        text: message,
        timestamp: userTimestamp
    });
    saveChatHistory();

    // ---- Clear input ----
    input.value = "";
    updateSendButton();

    try {
        // ---- Show typing indicator ----
        showTypingIndicator();

        console.log("Sending message to backend:", message);

        const response = await fetch("/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: message })
        });

        if (!response.ok) {
            throw new Error("Server returned HTTP " + response.status);
        }

        const data = await response.json();
        console.log("Backend response:", data);

        if (!data.response) {
            throw new Error("Backend did not return a response.");
        }

        // ---- Small delay for natural feel ----
        await new Promise(resolve => setTimeout(resolve, 350));

        hideTypingIndicator();

        const botTimestamp = getCurrentTime();

        addBotMessage(data.response, botTimestamp);

        chatHistory.push({
            sender: "bot",
            response: data.response,
            intent: data.intent || null,
            topic: data.topic || null,
            suggestions: data.suggestions || [],
            timestamp: botTimestamp
        });
        saveChatHistory();

        if (Array.isArray(data.suggestions) && data.suggestions.length > 0) {
            addSuggestions(data.suggestions, message);
        }

        scrollToBottom();

    } catch (error) {
        console.error("Chat error:", error);
        hideTypingIndicator();

        const errorResponse = ["Sorry, something went wrong. Please try again."];
        const errorTimestamp = getCurrentTime();

        addBotMessage(errorResponse, errorTimestamp);

        chatHistory.push({
            sender: "bot",
            response: errorResponse,
            intent: "error",
            topic: null,
            suggestions: [],
            timestamp: errorTimestamp
        });
        saveChatHistory();

    } finally {
        isSending = false;
        updateSendButton();
        input.focus();
    }
}