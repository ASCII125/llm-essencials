"""
Interfaces for LLM
"""

from typing import List, Optional
from abc import ABC, abstractmethod

from .schemas import Message


class IAgent(ABC):
    """
    Agent interface class
    """

    @abstractmethod
    async def send_message(self, message: Message, context: Optional[List[Message]] = None) -> Message:
        """
        Send message to LLM with Optional context
        """