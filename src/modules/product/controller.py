from src.modules.product.services import ProductService
from fastapi import HTTPException
from src.core.database import SessionDep
from src.modules.product.schemas import ProductCreate
class ProductController:
    @staticmethod
    async def create_product(payload : ProductCreate, session : SessionDep):
        product = await ProductService.create_product(payload , session)
        return product

    @staticmethod
    async def get_all_products(session : SessionDep):
        product = await ProductService.get_all_products(session)
        return product

    @staticmethod
    async def get_by_id(id: int, session : SessionDep):
        product = await ProductService.get_by_id(id, session)
        if not product:
            raise HTTPException(status_code=404, detail="product not found")
        return product
