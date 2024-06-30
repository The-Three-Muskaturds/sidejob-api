from db.database import Base

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, DateTime, func
from datetime import datetime

class BaseModel(Base):
    """Basic implementation for all other models"""
    __abstract__ = True
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone = True), default = func.utc_timestamp()
    )
    modified_at: Mapped[datetime] = mapped_column(
        DateTime(timezone = True), nullable = True,  onupdate = func.utc_timestamp()
    )
    