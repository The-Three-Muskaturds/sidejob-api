from .base import BaseModel
from datetime import datetime
from sqlalchemy import Integer, String, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .user import User

class Project(BaseModel):
    """Model for the free-lancers prpojects?"""
    __tablename__ = "projects"

    project_name: Mapped[String] = mapped_column(String(32), unique=False, nullable=False)

    starting_at: Mapped[datetime] = mapped_column(
        DateTime(timezone = True), default = func.utc_timestamp()
    )
        
    ending_at: Mapped[datetime] = mapped_column(
        DateTime(timezone = True), nullable = False,  default = func.utc_timestamp()
    )

    user: Mapped["User"] = relationship(back_populates="projects")
    