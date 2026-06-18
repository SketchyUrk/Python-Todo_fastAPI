from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from json import dump, load, JSONDecodeError
from os import path

app = FastAPI()

TASKS_FILE = "tasks.json"

class TaskCreate(BaseModel):
    title: str
    
def load_tasks():
    if not path.exists(TASKS_FILE):
        return []
    
    try:
        with open(TASKS_FILE, "r") as file:
            return load(file)
    except (JSONDecodeError, FileNotFoundError):
        return []
    