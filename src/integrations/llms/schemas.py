"""
Schemas for LLM
"""

from typing import Literal

from pydantic import BaseModel


class Message(BaseModel):
    """
    Message Schema
    """
    role: Literal['user', 'assistant', 'system']
    content: str
