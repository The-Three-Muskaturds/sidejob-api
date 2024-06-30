from db.database import Base
from extensions import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, DateTime, func
from datetime import datetime


class BaseModel(db.Model, Base):
    __abstract__ = True

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=datetime.now
    )
    modified_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=True, onupdate=datetime.now
    )
