# agents.py
import asyncio
from typing import Any

class Agent:
    """
    Lightweight Agent wrapper that calls a given async model function.
    model_fn should be: async def model_fn(prompt: str, **kwargs) -> str
    """
    def __init__(self, name: str, instructions: str, model_fn: Any):
        self.name = name
        self.instructions = instructions.strip()
        self.model_fn = model_fn

    async def run(self, user_input: str, run_config: dict):
        """
        Calls the model function with a composed prompt (instructions + user_input).
        Returns an object with attribute `final_output` (string) to match earlier examples.
        """
        prompt = f"{self.instructions}\n\nUser: {user_input}"
        text = await self.model_fn(prompt, run_config=run_config)
        return type("Result", (), {"final_output": text})

    async def handoff(self, other_agent, user_input: str, run_config: dict):
        """
        Simple handoff — directly call the other agent's run.
        """
        return await other_agent.run(user_input, run_config)

class Runner:
    @staticmethod
    async def run(agent: Agent, user_input: str, run_config: dict):
        return await agent.run(user_input, run_config)
