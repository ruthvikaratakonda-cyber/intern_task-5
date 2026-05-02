from fastapi import APIRouter
from app.services.product_service import get_products

router = APIRouter()

@router.get("/")
def fetch_products():
    return get_products()