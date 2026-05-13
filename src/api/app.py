"""
Entry point API FastAPI
"""

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

from .routers import router


app = FastAPI(
    title="LLM Essentials",
    description="LLM Essentials API",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="resources/static"), name="static")
@app.get("/", response_class=HTMLResponse)
async def root():
    with open("resources/templates/index.html", "r") as f:
        return f.read()

app.include_router(router, prefix="/llm")
