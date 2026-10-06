from fastapi import APIRouter, HTTPException
from typing import Literal
from pydantic import BaseModel, Field

router = APIRouter(prefix="/tasks", tags=["Tasks"])

tasks = []

class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    priority: Literal["low", "medium", "high"] = "medium"

@router.get("/")
def get_tasks():
    return {"tasks": tasks}

@router.post("/")
def create_task(task: TaskCreate):
    new_task = {
        "id": len(tasks)+1,
        "title":  task.title,
        "priority": task.priority,
        "completed": False
    }

    tasks.append(new_task)

    return {
        "message":"Task created successfully",
        "task": new_task
    }

@router.get("/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return {"task": task}

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )