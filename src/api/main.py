from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.config.settings import get_settings
from src.api.routes import chat, analytics

settings = get_settings()
app = FastAPI(title=settings.APP_NAME)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(chat.router, tags=["Chat"])
app.include_router(analytics.router, tags=["Analytics"])

@app.get("/")
def health():
    return {"status": "ok", "service": settings.APP_NAME}
