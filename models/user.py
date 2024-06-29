from models.base import Base

from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer, String, DateTime
from sqlalchemy.sql import func

class User(Base):
    __tablename__ = "user"

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    username = mapped_column(String(255), nullable=False)
    email = mapped_column(String(255), nullable=False)
    password = mapped_column(String(255), nullable=False)
    role = mapped_column(String(100))
    created_at = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())