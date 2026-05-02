from fastapi import APIRouter
from app.schemas.user_schema import UserCreate
from app.services.user_service import create_user

router = APIRouter()

@router.post("/")
def register(user: UserCreate):
    return create_user(user)