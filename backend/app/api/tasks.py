from fastapi import APIRouter,Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate, TaskResponse, TaskUpdateResponse

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

@router.get("/", response_model=list[TaskResponse])
def get_tasks(db: Session = Depends(get_db)):
    tasks = db.query(Task).all()
    return tasks

@router.post("/", response_model=TaskResponse, status_code=201)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    new_task = Task(
        title=task.title,
        priority=task.priority
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task

@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()

    if task is None:
        raise HTTPException(
                status_code=404,
                detail="Task not found"
            )

    return task


@router.patch("/{task_id}", response_model= TaskUpdateResponse)
def update_task(
    task_id: int, 
    task_update: TaskUpdate,
    db: Session = Depends(get_db)
):

    task = db.query(Task).filter(Task.id == task_id).first()

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    update_data = task_update.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(task, key, value)

    db.commit()
    db.refresh(task)

    return {"message": "Task updated successfully",
            "updated_task": task}

@router.delete("/{task_id}", response_model=TaskUpdateResponse)
def delete_task(task_id: int, db: Session = Depends(get_db)):

        task = db.query(Task).filter(Task.id == task_id).first()

        if task is None:
            raise HTTPException(
                    status_code=404,
                    detail="Task not found"
            )

        deleted_task = TaskResponse.model_validate(task)

        db.delete(task)
        db.commit()

        return {
            "message": "Task deleted successfully",
            "updated_task": deleted_task
        }