from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.user import User
from app.auth.hash import hash_password

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
def register(
    username: str,
    email: str,
    password: str,
    db: Session = Depends(get_db)
):

    user = User(
        username=username,
        email=email,
        password=hash_password(password)
    )

    db.add(user)
    db.commit()

    return {"message": "User created"}
