from datetime import datetime
from sqlalchemy import String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import BaseModel
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .user import User


class Project(BaseModel):
    """Model for the freelancers projects"""

    __tablename__ = "projects"

    project_name: Mapped[str] = mapped_column(String(32), unique=False, nullable=False)

    start_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=datetime.now
    )

    end_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, default=datetime.now
    )
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship("User", back_populates="projects")

    def __init__(
        self, project_name: str, start_date: datetime, end_date: datetime, user_id: int
    ):
        self.project_name = project_name
        self.start_date = start_date
        self.end_date = end_date
        self.user_id = user_id
