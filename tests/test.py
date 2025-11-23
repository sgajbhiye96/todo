# ...existing code...

import os
import sys

# Ensure repository root is on sys.path so `from app import app` can be imported by tests
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
from app import app

client = app.test_client()

def test_home():
    res = client.get("/")
    assert res.status_code == 200

def test_create_todo():
    data = {"task": "Learn Flask"}
    res = client.post("/todo", json=data)
    assert res.status_code == 201
    assert res.get_json()["status"] == "created"

def test_get_todos():
    res = client.get("/todo")
    assert res.status_code == 200

def test_update_todo():
    data = {"task": "Updated task"}
    res = client.put("/todo/0", json=data)
    assert res.status_code == 200

def test_delete_todo():
    res = client.delete("/todo/0")
    assert res.status_code == 200
# ...existing code...