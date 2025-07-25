from typing import Optional, Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.entities import TaskStatus
from src.models import Task
from src.schemas import TaskCreate, TaskUpdate


class TaskRepository:
    @staticmethod
    async def get_one(db: AsyncSession, task_id: int) -> Optional[Task]:
        result = await db.execute(select(Task).where(Task.id == task_id))
        return result.scalar_one_or_none()

    @staticmethod
    async def get_all(
            db: AsyncSession,
            status: Optional[TaskStatus] = None,
            skip: int = 0,
            limit: int = 100
    ) -> Sequence[Task]:
        query = select(Task)
        if status:
            query = query.where(Task.status == status)
        query = query.offset(skip).limit(limit)
        result = await db.execute(query)
        return result.scalars().all()

    @staticmethod
    async def create(db: AsyncSession, task_in: TaskCreate) -> Task:
        db_task = Task(
            title=task_in.title,
            description=task_in.description,
            status=task_in.status,
        )
        db.add(db_task)
        await db.commit()
        await db.refresh(db_task)
        return db_task

    @staticmethod
    async def update(db: AsyncSession, db_task: Task, task_in: TaskUpdate) -> Task:
        if task_in.title is not None:
            db_task.title = task_in.title
        if task_in.description is not None:
            db_task.description = task_in.description
        if task_in.status is not None:
            db_task.status = task_in.status
        await db.commit()
        await db.refresh(db_task)
        return db_task

    @staticmethod
    async def delete(db: AsyncSession, db_task: Task) -> None:
        await db.delete(db_task)
        await db.commit()
