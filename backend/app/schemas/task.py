from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    priority: str = "Medium"

class TaskUpdate(BaseModel):
    title: str | None = None
    priority: str | None = None
    completed: bool | None = None

class TaskResponse(BaseModel):
    id: int
    title: str
    priority: str
    completed: bool

    model_config = {
        "from_attributes": True
    }

class TaskUpdateResponse(BaseModel):
    message: str
    updated_task: TaskResponse