from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models import User, UserCreate, UserResponse
from sqlalchemy import func

router = APIRouter()


@router.post("/users/",
             response_model=UserResponse,
             status_code=201)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = (db.query(User).filter(func.lower(User.email) == func.lower(user.email)).first())
    if db_user:
        raise HTTPException(status_code=400, detail="email already registered")
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.get("/users/", response_model=List[UserResponse])
def read_users(skip: int = 0, limit: int = 10,
               db: Session = Depends(get_db)):
    users = db.query(User).offset(skip).limit(limit).all()
    return users


@router.get("/users/{user_id}", response_model=UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="user not found")
    return db_user
