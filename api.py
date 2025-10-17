from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Any

app = FastAPI()

class TaskRequest(BaseModel):
    email: str
    secret: str
    task: str
    round: int
    nonce: str
    brief: str
    checks: List[str]
    evaluation_url: str
    attachments: List[Any]

@app.post("/api-endpoint")
def receive_task(payload: TaskRequest):
    # Echo the received data
    return {
        "status": "ok",
        "received": payload.dict()
    }

@app.get("/")
def root():
    return {"message": "FastAPI server is running!"}


