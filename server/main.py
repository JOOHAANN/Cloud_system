from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title = "First Local Service")

class Command(BaseModel):
    robot_id: str
    command: str

@app.get("/health")
def health_check():
    return {"status": "ok", "message": "Service is running"}

@app.get("/robot/status")
def robot_status():
    return {"robot_id": "robot_01", "battery": "80%", "ready": True}

@app.post("/robot/command")
def send_command(data: Command):
    return {"robot_id": data.robot_id, "command": data.command, "result": "Command received"}