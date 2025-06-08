from sqlalchemy import Column, Integer, String, Enum
from app.core.database import Base
import enum


# Define user roles (admin or regular user)
class UserRole(enum.Enum):
    admin = "admin"
    user = "user"


# This class maps to the "users" table in the database
class User(Base):
    __tablename__ = "users"  # Table name in the DB

    id = Column(Integer, primary_key=True, index=True)  # Unique identifier
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)  # Emails must be unique
    hashed_password = Column(String, nullable=False)
    role = Column(Enum(UserRole), default=UserRole.user)  # Admin/User role
