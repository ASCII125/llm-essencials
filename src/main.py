"""
Entry point module
"""

import uvicorn

from api.app import app

from setup import setup


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=setup.API_PORT)
