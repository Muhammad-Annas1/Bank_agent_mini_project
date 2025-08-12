# main.py
import asyncio
from agents_setup import bank_agent, account_agent, loan_agent, config
from agents import Runner
from utils import input_guardrails, output_guardrails

async def main():
    user_input = input("💬 Welcome to ABC Bank! How can I help you today? ")

    ok, reason = input_guardrails(user_input)
    if not ok:
        print(f"⚠️ Invalid input: {reason}")
        return

    # Step 1: classify using bank_agent
    classification_run = await Runner.run(bank_agent, user_input, run_config=config)
    intent = classification_run.final_output.strip().lower()
    print(f"📌 Detected intent: {intent}")

    # Step 2: handoff based on intent
    if intent == "account":
        agent_result = await bank_agent.handoff(account_agent, user_input, run_config=config)
        safe_output = output_guardrails(agent_result.final_output)
        print(f"🏦 Account Info: {safe_output}")

    elif intent == "loan":
        agent_result = await bank_agent.handoff(loan_agent, user_input, run_config=config)
        safe_output = output_guardrails(agent_result.final_output)
        print(f"💰 Loan Info: {safe_output}")

    else:
        print("❌ Sorry, I can only help with 'account' or 'loan' queries. Please rephrase or contact support.")

if __name__ == "__main__":
    asyncio.run(main())
