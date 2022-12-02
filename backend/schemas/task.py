from typing import List

from fastapi import APIRouter

import backend.schemas.task as task_schema

router = APIRouter()

@router.get("/tasks")
async def list_tasks():
    pass
@router.get("/tasks", response_model=List[task_schema.Task])
async def list_tasks():
    return [task_schema.Task(id=1, title="1つ目のTODOタスク")]