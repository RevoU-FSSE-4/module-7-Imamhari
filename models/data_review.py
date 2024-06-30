from models.base import Base
from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer, String, DateTime, Text
from sqlalchemy.sql import func

class Review(Base):
    __tablename__ = "data_review"
    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    email = mapped_column(String(50), nullable=False)
    rating = mapped_column(Integer, nullable=False)
    description = mapped_column(Text, nullable=False)
    created_at = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now())