from datetime import datetime
from sqlalchemy import String, DateTime, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import BaseModel


class Project(BaseModel):
    """Model for the free-lancers prpojects?"""

    __tablename__ = "projects"

    project_name: Mapped[String] = mapped_column(
        String(32), unique=False, nullable=False
    )

    start_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=datetime.now
    )

    end_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, default=datetime.now
    )
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="projects")

    def __init__(self, project_name, start_date, end_date, user_id):
        self.project_name = (project_name,)
        self.start_date = start_date
        self.end_date = end_date
        self.user_id = user_id
