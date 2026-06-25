from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.routers import transaction, summary, ranking

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Reward Ranking API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(transaction.router)
app.include_router(summary.router)
app.include_router(ranking.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # For assignment/demo only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Reward Ranking API is running"}