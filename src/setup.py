"""
Configuration module
"""

from dotenv import dotenv_values

from integrations.llms import GroqAgent


class Setup:
    """
    Configuration variables
    """

    def __init__(self):
        self.config = dotenv_values(".env")
        self.API_PORT = self.config.get("API_PORT", 8000)
        self.GROQ_KEY = self.config["GROQ_KEY"]

setup = Setup()
groq_agent = GroqAgent(groq_key=setup.GROQ_KEY)
