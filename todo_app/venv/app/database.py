import json
from typing import List, Dict
from pathlib import Path

DATABASE_PATH = Path("tasks.json")

def read_database() -> Dict[int, Dict]:
    if DATABASE_PATH.exists():
        with open(DATABASE_PATH, "r") as file:
            return json.load(file)
    return {}

def write_database(data: Dict[int, Dict]):
    with open(DATABASE_PATH, "w") as file:
        json.dump(data, file, indent=4)

db = read_database()
current_id = max((int(key) for key in db.keys()), default=0) + 1 if db else 1



def get_all_tasks() -> List[Dict]:
    return list(db.values())

def get_task_by_id(task_id: int) -> Dict:
    return db.get(task_id)

def create_task(task: Dict) -> Dict:
    global current_id
    task["id"] = current_id
    db[current_id] = task
    current_id += 1
    write_database(db)
    return task

def update_task(task_id: int, updated_task: Dict) -> Dict:
    if task_id in db:
        db[task_id].update(updated_task)
        write_database(db)
        return db[task_id]
    return None

def delete_task(task_id: int) -> bool:
    if task_id in db:
        del db[task_id]
        write_database(db)
        return True
    return False
