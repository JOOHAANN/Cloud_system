import requests

BASE_URL = "http://127.0.0.1:8000"

health = requests.get(f"{BASE_URL}/health")

print("Health Check:", health.json())

status = requests.get(f"{BASE_URL}/robot/status")
print("Robot Status:", status.json())

payload = {"robot_id": "robot_01", "command": "move_forward"}
response = requests.post(f"{BASE_URL}/robot/command", json=payload)
print("Command Response:", response.json())