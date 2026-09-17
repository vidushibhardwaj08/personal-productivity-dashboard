from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Personal Productivity Dashboard API"}

@app.get("/health")
def health():
     return {"status": "healthy"}