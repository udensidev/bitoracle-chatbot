# src/bitoracle.py

import os
import gradio as gr
import yfinance as yf
import google.generativeai as genai
from dotenv import load_dotenv

# --- CONFIGURATION ---
# Load API key from environment variable or fallback to hardcoded string
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "YOUR_API_KEY_HERE")

if GEMINI_API_KEY == "YOUR_API_KEY_HERE":
    raise ValueError("❌ Please set your Gemini API key in the script or as an environment variable.")

genai.configure(api_key=GEMINI_API_KEY)

# --- HELPER FUNCTIONS ---

def fetch_bitcoin_prices():
    """Fetch Bitcoin daily closing prices for the last 10 days."""
    btc = yf.download('BTC-USD', period="10d", interval="1d")
    price_list = [f"{index.strftime('%Y-%m-%d')}: ${float(row['Close'].iloc[0]):.2f}" for index, row in btc.iterrows()]
    return "\n".join(price_list)

def create_prompt(prices_text, user_question):
    """Create the full prompt for Gemini, embedding Bitcoin prices."""
    return f"""Bitcoin daily closing prices:
{prices_text}

Question:
Think step-by-step and explain your reasoning. {user_question}
"""

def chatbot_response(user_input, history):
    """Handle user interaction and generate response using Gemini."""
    if not user_input.strip():
        return history, history, ""  # Skip empty input

    # Create prompt using the latest Bitcoin prices
    prompt = create_prompt(PRICES_TEXT, user_input)
    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content(prompt)

    # Append user message and bot response as dictionaries
    history.append({"role": "user", "content": user_input})
    history.append({"role": "assistant", "content": response.text})

    return history, history, ""  # Clear the input box

# --- MAIN APP ---

# Fetch Bitcoin prices once at startup
PRICES_TEXT = fetch_bitcoin_prices()

with gr.Blocks() as demo:
    gr.Markdown("""
# 💬 Welcome to BitOracle

I'm your crypto companion! 🚀  
Ask me anything about Bitcoin prices, trends, or recent market movements.

Here are some ideas you can try:
- 🪙 "What was Bitcoin's price 3 days ago?"
- 📈 "What's the average Bitcoin price over the past week?"
- 🔍 "Has Bitcoin been trending upward or downward?"

I'm ready whenever you are — just type your question below! 👇
        """)

    chatbot_output = gr.Chatbot(type='messages')
    user_input = gr.Textbox(placeholder="Ask about Bitcoin prices...")
    state = gr.State([])

    user_input.submit(chatbot_response, [user_input, state], [chatbot_output, state, user_input])

# --- LAUNCH APP ---

if __name__ == "__main__":
    demo.launch(share=True)
