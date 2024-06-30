from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import BaseModel
from typing import List


class User(BaseModel):
    __tablename__ = "users"

    first_name: Mapped[str] = mapped_column(String(32), unique=False, nullable=False)
    last_name: Mapped[str] = mapped_column(String(32), unique=False, nullable=False)
    username: Mapped[str] = mapped_column(String(80), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(80), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(512), nullable=False)
    projects: Mapped[List["Project"]] = relationship("Project", back_populates="user")

    def __init__(self, first_name, last_name, username, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
