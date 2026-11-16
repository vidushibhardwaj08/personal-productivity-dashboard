from fastapi import APIRouter, HTTPException
from typing import Literal
from pydantic import BaseModel, Field

router = APIRouter(prefix="/tasks", tags=["Tasks"])

tasks = []

class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    priority: Literal["low", "medium", "high"] = "medium"

class TaskUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=200)
    priority: Literal["low", "medium", "high"] | None = None
    completed: bool | None = None

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

@router.patch("/{task_id}")
def update_task(task_id: int, task_update: TaskUpdate):
    for task in tasks:
        if task["id"] == task_id:

            if task_update.title is not None:
                task["title"] = task_update.title

            if task_update.priority is not None:
                task["priority"] = task_update.priority

            if task_update.completed is not None:
                task["completed"] = task_update.completed