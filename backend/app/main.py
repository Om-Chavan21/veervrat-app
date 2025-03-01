from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import virtues, weaknesses, questions

app = FastAPI(title="Virtues and Weaknesses Mapping API", version="1.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(virtues.router, prefix="/api", tags=["Virtues"])
app.include_router(weaknesses.router, prefix="/api", tags=["Weaknesses"])
app.include_router(questions.router, prefix="/api", tags=["Questions"])


@app.get("/", tags=["Root"])
async def root():
    return {
        "message": "Welcome to the Virtues and Weaknesses Mapping API",
        "docs": "/docs",
    }
