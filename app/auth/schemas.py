from pydantic import BaseModel, EmailStr
from enum import Enum


# Enum for user roles
class UserRole(str, Enum):
    admin = "admin"
    user = "user"


# Schema for user registration
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: UserRole = UserRole.user


# Schema for login request
class UserLogin(BaseModel):
    email: EmailStr
    password: str


# Schema for returning user data (excluding password)
class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: UserRole

    class Config:
        orm_mode = True  # Needed to work with SQLAlchemy models
