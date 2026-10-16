from fastapi import FastAPI  # type: ignore[import-not-found]
from fastapi.middleware.cors import CORSMiddleware # type: ignore[import-not-found]
from core.config import settings

app = FastAPI(
    title="Be the Hero API",
    description="API for Be the hero of our own adventure",
    version="1.0.0",
    docs_url="/docs",
    redocs_url="/redocs",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)    


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
