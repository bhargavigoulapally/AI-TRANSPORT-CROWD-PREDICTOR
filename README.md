# 🤖 Gemini AI Chatbot

A simple and interactive **AI chatbot built with Python, Streamlit, and Google Gemini API**.
The application allows users to enter questions or prompts and receive intelligent AI-generated responses.

## 🚀 Live Demo

Add your deployed Streamlit URL here:

**🔗 Live Demo:** `https://your-app-name.streamlit.app/`

## ✨ Features

* 🤖 AI-powered responses using Google Gemini
* 💬 Simple and user-friendly interface
* ⚡ Fast response generation
* 🎨 Clean Streamlit UI
* 🔐 Secure API key configuration
* 📱 Responsive interface
* 🧠 Supports general questions and AI prompts

## 🛠️ Technologies Used

* **Python**
* **Streamlit**
* **Google Gemini API**
* **Google GenAI SDK**
* **python-dotenv** (for local development)

## 📁 Project Structure

```text
gemini-ai-chatbot/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── .streamlit/
    └── secrets.toml
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/gemini-ai-chatbot.git
```

```bash
cd gemini-ai-chatbot
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 🔑 API Key Configuration

### Local Development

Create:

```text
.streamlit/secrets.toml
```

Add your Gemini API key:

```toml
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
```

**Do not upload `secrets.toml` to GitHub.**

Add this to `.gitignore`:

```text
.streamlit/secrets.toml
.env
venv/
__pycache__/
```

### Streamlit Cloud

In your Streamlit Cloud application:

**Settings → Secrets**

Add:

```toml
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
```

Your Python code can then access it using:

```python
import streamlit as st

api_key = st.secrets["GEMINI_API_KEY"]
```

## ▶️ Run the Application

Start the application with:

```bash
streamlit run app.py
```

The application will open in your browser.

## 💡 Example Prompt

```text
Explain Artificial Intelligence in simple words.
```

The Gemini model will generate an AI-powered response.

## 🔐 Security

**Never expose your Gemini API key publicly.**

Do not put API keys directly inside:

* `app.py`
* `README.md`
* GitHub repositories
* screenshots
* GitHub Issues
* public deployment logs

If an API key has accidentally been published, **revoke it and create a new key immediately**.

## 📌 Future Improvements

* 💬 Chat history
* 🎙️ Voice input
* 🔊 Text-to-speech
* 📄 PDF question answering
* 🖼️ Image understanding
* 🌐 Multi-language support
* 👤 User authentication
* 💾 Conversation storage

## 👩‍💻 Author

**Bhargavi**

B.Tech – Artificial Intelligence & Machine Learning

---

⭐ If you like this project, consider giving the repository a star!
