from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

class TaskRequest(BaseModel):
    email: str
    secret: str
    task: str
    round: int
    nonce: str
    brief: str
    checks: list
    evaluation_url: str
    attachments: list

@app.post("/api-endpoint")
async def receive_task(request: Request):
    data = await request.json()
    # TODO: Validate secret, process brief, generate repo, etc.
    return {"status": "received", "message": "Task received and being processed."}

