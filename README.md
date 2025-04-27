# 💬 BitOracle Chatbot

**BitOracle** is an interactive crypto chatbot powered by Google Gemini.  
It answers dynamic questions about Bitcoin prices using real-world data and step-by-step AI reasoning.

---

## 📜 Project Overview

This project:
- Fetches live Bitcoin price data from Yahoo Finance.
- Embeds real price data inside the AI's prompt.
- Allows users to ask questions like:
  - 🪙 "What was Bitcoin's price 3 days ago?"
  - 📈 "What's the average Bitcoin price over the past week?"
  - 🔍 "Has Bitcoin been trending up or down?"
- Responds using **Google Gemini** for step-by-step reasoning.
- Runs inside a clean Gradio chatbot web app.

---

## 🏗️ Folder Structure

```
bitoracle-chatbot/
├── app.py
├── requirements.txt
├── README.md
├── launch_chatbot.sh
```

---

## 🛠️ Setup Instructions

1. Clone or download this repository.

2. Set your **Gemini API key**:
   - Option 1: Edit `app.py` and replace `"YOUR_API_KEY_HERE"`.
   - Option 2 (recommended): Set an environment variable:
     ```
     export GEMINI_API_KEY="your-real-api-key"
     ```

3. Run the launch script:

```bash
bash launch_chatbot.sh
```

✅ This will automatically:
- Check for and install Python dependencies
- Open a Gradio app in your web browser.

---

## 📚 Technologies Used

- Python 3.10+
- `gradio` (chatbot interface)
- `google-generativeai` (Gemini-Pro model)
- `yfinance` (Bitcoin price data fetching)

---

## 🚀 Features

- Real-time Bitcoin data embedded inside AI prompts
- Gemini step-by-step reasoning and conversational answers
- Auto-clears textbox after user message for smooth UX
- Friendly welcome message and example questions
- Local web-based interface via Gradio
- Lightweight and easy to launch

---

## 📣 Attribution

- Live Bitcoin price data sourced from [Yahoo Finance](https://finance.yahoo.com/crypto/).
- AI reasoning powered by **Google Gemini** under API usage limits.



