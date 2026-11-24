from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import tasks
from app.db.database import engine, Base
from app.models import task

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(tasks.router)

@app.get("/")
def root():
    return {"message": "Personal Productivity Dashboard API"}

@app.get("/health")
def health():
    return {"status": "healthy"}

