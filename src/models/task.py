from datetime import datetime

from sqlalchemy import Enum as SQLEnum, DateTime, func
from sqlalchemy.orm import mapped_column, Mapped

from src.entities import TaskStatus
from src.models import Base


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    description: Mapped[str | None]
    status: Mapped[TaskStatus] = mapped_column(SQLEnum(TaskStatus))

    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
