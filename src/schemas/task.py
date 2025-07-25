from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from src.entities import TaskStatus


class TaskBase(BaseModel):
    title: str = Field(..., max_length=255)
    description: Optional[str] = None
    status: TaskStatus = TaskStatus.pending


class TaskCreate(TaskBase):
    pass


class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, max_length=255)
    description: Optional[str] = None
    status: Optional[TaskStatus] = None


class TaskInDBBase(TaskBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class TaskOut(TaskInDBBase):
    pass
