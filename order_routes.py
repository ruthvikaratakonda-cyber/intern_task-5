from fastapi import APIRouter
from app.services.order_service import create_order

router = APIRouter()

@router.post("/")
def place_order(order: dict):
    return create_order(order)