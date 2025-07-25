from typing import Optional

from fastapi import APIRouter, status, Depends, Query, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.session import get_session
from src.entities import TaskStatus
from src.repositories.task_repository import TaskRepository
from src.schemas import TaskOut, TaskCreate, TaskUpdate

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.post("/", response_model=TaskOut, status_code=status.HTTP_201_CREATED)
async def create_task(
    task_in: TaskCreate,
    db: AsyncSession = Depends(get_session)
):
    return await TaskRepository.create(db, task_in)


@router.get("/", response_model=list[TaskOut])
async def list_tasks(
    task_status: Optional[TaskStatus] = Query(None),
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_session)
):
    return await TaskRepository.get_all(db, status=task_status, skip=skip, limit=limit)


@router.get("/{task_id}", response_model=TaskOut)
async def get_task(
    task_id: int,
    db: AsyncSession = Depends(get_session)
):
    task = await TaskRepository.get_one(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.put("/{task_id}", response_model=TaskOut)
async def update_task(
    task_id: int,
    task_in: TaskUpdate,
    db: AsyncSession = Depends(get_session)
):
    task = await TaskRepository.get_one(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return await TaskRepository.update(db, task, task_in)


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(
    task_id: int,
    db: AsyncSession = Depends(get_session)
):
    task = await TaskRepository.get_one(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    await TaskRepository.delete(db, task)