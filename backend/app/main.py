from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.routers import transaction, summary, ranking

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Reward Ranking API",
    description="Backend for Reward Ranking Assignment",
    version="1.0.0"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # For assignment/demo
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(transaction.router)
app.include_router(summary.router)
app.include_router(ranking.router)

@app.get("/")
def root():
    return {
        "message": "Reward Ranking API is running",
        "status": "healthy"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }