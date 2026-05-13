"""
Routers APP
"""

from fastapi import APIRouter, Body

from setup import groq_agent
from integrations.llms import Message


router = APIRouter()


@router.post("/chat", response_model=Message)
async def chat(message: str = Body(..., description="Message to send to LLM", embed=True)):
    """
    Chat endpoint
    """
    rmessage = await groq_agent.send_message(Message(role="user", content=message))
    return rmessage