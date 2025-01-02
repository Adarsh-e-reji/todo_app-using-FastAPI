from fastapi import FastAPI, HTTPException
from app.models import Task, TaskUpdate  
from app.database import get_all_tasks, get_task_by_id, create_task, update_task, delete_task
from typing import List

app = FastAPI() #initialize fastapi

@app.post("/tasks", response_model=Task)
def create_new_task(task: Task):
    new_task = create_task(task.dict())
    return new_task

@app.get("/tasks", response_model=List[Task])
def fetch_all_tasks():
    return get_all_tasks()

@app.get("/tasks/{task_id}", response_model=Task)
def fetch_task_by_id(task_id: int):
    task = get_task_by_id(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.put("/tasks/{task_id}", response_model=Task)
def update_task_status(task_id: int, task_update: TaskUpdate):
    updated_task = update_task(task_id, {"status": task_update.status})
    if not updated_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task

@app.delete("/tasks/{task_id}", response_model=dict)
def delete_task_by_id(task_id: int):
    if not delete_task(task_id):
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted successfully"}
