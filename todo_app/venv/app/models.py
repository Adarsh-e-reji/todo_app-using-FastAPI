from pydantic import BaseModel
from typing import Optional

class Task(BaseModel):
    title: str
    description: str
    status: Optional[str] = "pending"  

    class Config:
        orm_mode = True

class TaskUpdate(BaseModel):
    status: str 