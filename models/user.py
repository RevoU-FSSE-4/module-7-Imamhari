from models.base import Base

from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer, String, DateTime
from sqlalchemy.sql import func
from flask_login import UserMixin
import bcrypt

class User(Base, UserMixin):
    __tablename__ = "user"

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    username = mapped_column(String(255), nullable=False)
    email = mapped_column(String(255), nullable=False)
    password = mapped_column(String(255), nullable=False)
    role = mapped_column(String(100))
    created_at = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())

    def set_password(self, password):
        self.password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, password):
        return bcrypt.checkpw(password.encode("utf-8"), self.password.encode("utf-8"))