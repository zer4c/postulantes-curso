from src.modules.product.services import ProductService
from fastapi import HTTPException


class ProductController:
    @staticmethod
    def create_product():
        product = ProductService.create_product()
        return {
            "message": "Product created",
            "data": product,
            "ok": True,
        }

    @staticmethod
    def get_all_products():
        product = ProductService.get_all_products()
        return {
            "message": "Products retrieved",
            "data": product,
            "ok": True,
        }

    @staticmethod
    def get_by_id(id: int):
        product = ProductService.get_by_id(id)
        if not product:
            raise HTTPException(status_code=404, detail="product not found")
        return {
            "message": "Product retrieved",
            "data": product,
            "ok": True,
        }
