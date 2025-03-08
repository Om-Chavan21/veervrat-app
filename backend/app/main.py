from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import (
    main_virtues,
    sub_virtues,
    weaknesses,
    questions,
    dals,
    users,
    questionnaires,
)

app = FastAPI(title="Virtues and Weaknesses Mapping API", version="1.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],  # Add your frontend URLs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(users.router, prefix="", tags=["Users"])
app.include_router(main_virtues.router, prefix="", tags=["Main Virtues"])
app.include_router(sub_virtues.router, prefix="", tags=["Sub Virtues"])
app.include_router(weaknesses.router, prefix="", tags=["Weaknesses"])
app.include_router(questions.router, prefix="", tags=["Questions"])
app.include_router(dals.router, prefix="", tags=["Dals"])
app.include_router(
    questionnaires.router, prefix="", tags=["Questionnaires"]
)  # Add this line


@app.get("/", tags=["Root"])
async def root():
    return {
        "message": "Welcome to the Virtues and Weaknesses Mapping API",
        "docs": "/docs",
    }
