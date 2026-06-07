from fastapi import APIRouter
from src.modules.product.controller import ProductController

router = APIRouter()

@router.get("/")
def get_all_product():
    return ProductController.get_all_products()

@router.get("/{id}")
def get_by_id(id : int):
    return ProductController.get_by_id(id)

@router.post("/")
def create_product():
    return ProductController.create_product()