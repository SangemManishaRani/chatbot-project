# 🤖 AI Chatbot using Python + OpenAI

This is a simple terminal-based AI chatbot built using Python and the OpenAI API.

---

## 🛠 Features

- Uses GPT-3.5-turbo via OpenAI
- Runs in terminal
- Keeps API key hidden using `.env` file
- Easy setup for evaluators

---

## 🚀 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/chatbot-project.git
cd chatbot-project
```

### 2. Create `.env` file

Copy `.env.example` to `.env`:

```bash
cp .env.example .env
```

Paste your OpenAI API key inside:

```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxx
```

### 3. Install dependencies

```bash
pip install openai python-dotenv
```

### 4. Run the chatbot

```bash
python chatbot.py
```

---

## 🧠 Built With

- Python
- OpenAI GPT (gpt-3.5-turbo)
- VS Code
