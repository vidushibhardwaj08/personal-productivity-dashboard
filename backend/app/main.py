from fastapi import FastAPI
from app.api import tasks

app = FastAPI()

app.include_router(tasks.router)

@app.get("/")
def root():
    return {"message": "Personal Productivity Dashboard API"}

@app.get("/health")
def health():
    return {"status": "healthy"}

