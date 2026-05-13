"""
Groq interface adapter
"""

from typing import List, Optional

from groq import AsyncGroq

from ..interfaces import IAgent
from ..schemas import Message


class GroqAgent(IAgent):
    """
    Groq Agent Adapter
    """
    
    def __init__(self, groq_key: str, model: str = "openai/gpt-oss-120b"):
        self.groq = AsyncGroq(api_key=groq_key)
        self.model = model

    async def send_message(self, message: Message, context: Optional[List[Message]] = None) -> Message:
        """
        Send message to LLM with Optional context
        """

        context = context or []
        context.append(message.model_dump())
        cchat = await self.groq.chat.completions.create(
            model=self.model,
            messages=context,
        )

        return Message(
            role=cchat.choices[0].message.role,
            content=cchat.choices[0].message.content
        )