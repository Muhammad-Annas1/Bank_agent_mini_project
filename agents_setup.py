# agents_setup.py
import os
import asyncio
from dotenv import load_dotenv
import google.generativeai as genai
from agents import Agent

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise EnvironmentError("GEMINI_API_KEY is missing. Create a .env file with GEMINI_API_KEY=...")

# Configure SDK
genai.configure(api_key=GEMINI_API_KEY)

# Helper model wrapper (async version)
async def gemini_model(prompt: str, run_config: dict):
    """
    Uses google.generativeai.GenerativeModel to call gemini-1.5-flash.
    Runs blocking SDK call inside a thread to avoid blocking event loop.
    """
    model_name = run_config.get("model", "models/gemini-1.5-flash")
    model = genai.GenerativeModel(model_name)

    def generate_sync(p):
        resp = model.generate_content(p)  # ✅ No 'prompt=' keyword
        # Safely extract text from response
        if hasattr(resp, "text") and resp.text:
            return resp.text
        try:
            return str(resp.result[0].output[0].content[0].text)
        except Exception:
            return str(resp)

    # ✅ Pass the prompt to the thread function
    text = await asyncio.to_thread(generate_sync, prompt)
    return text

# Run config
config = {
    "model": "models/gemini-1.5-flash",
}

# Agents
bank_agent = Agent(
    name="BankAgent",
    instructions=(
        "You are a bank assistant whose job is to classify the customer's request "
        "into one of three simple intents: 'account', 'loan', or 'other'.\n\n"
        "Output exactly one word: 'account', 'loan', or 'other'. No extra commentary."
    ),
    model_fn=gemini_model
)

account_agent = Agent(
    name="AccountAgent",
    instructions=(
        "You are an account help assistant. Provide a short, friendly answer (1-2 sentences) "
        "about account services (balance check, statements, account types). "
        "Do NOT include any real account numbers or sensitive data; mask digits if present."
    ),
    model_fn=gemini_model
)

loan_agent = Agent(
    name="LoanAgent",
    instructions=(
        "You are a loan help assistant. Provide a short, friendly answer (1-2 sentences) "
        "about loan options, typical interest ranges, and required documents. "
        "Do NOT ask for or include personal data in your reply."
    ),
    model_fn=gemini_model
)

# Export names
__all__ = ["bank_agent", "account_agent", "loan_agent", "config"]
