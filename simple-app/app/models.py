from sqlalchemy import Column, Integer, String
from app.database import Base
from pydantic import BaseModel, EmailStr


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    full_name = Column(String)


class UserCreate(BaseModel):
    email: EmailStr
    full_name: str


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    full_name: str

    class Config:
        orm_mode = True  # для удобства
