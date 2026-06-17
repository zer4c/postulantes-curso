from src.modules.product.services import ProductService
from fastapi import HTTPException
from src.core.database import SessionDep
from src.modules.product.schemas import ProductCreate, ProductPatch
from src.core.response_model import IResponse


class ProductController:
    @staticmethod
    async def create_product(payload: ProductCreate, session: SessionDep):
        product = await ProductService.create_product(payload, session)
        return IResponse(code=201, message="Product created", data=product)

    @staticmethod
    async def get_all_products(session: SessionDep, limit: int, offset: int):
        product = await ProductService.get_all_products(session, limit, offset)
        return IResponse(
            code=200,
            message="Products retrieved",
            data=product,
            limit=limit,
            offset=offset,
        )

    @staticmethod
    async def get_by_id(id: int, session: SessionDep):
        product = await ProductService.get_by_id(id, session)
        if not product:
            raise HTTPException(status_code=404, detail="product not found")
        return IResponse(
            code=200,
            message="Product retrieved",
            data=product,
        )

    @staticmethod
    async def delete_product(id: int, session: SessionDep):
        product = await ProductService.get_by_id(id, session)
        if not product:
            raise HTTPException(status_code=404, detail="product not found")
        await ProductService.delete_product(id, session)

    @staticmethod
    async def update_product(id: int, payload: ProductPatch, session: SessionDep):
        product = await ProductService.get_by_id(id, session)
        if not product:
            raise HTTPException(status_code=404, detail="product not found")
        new_product = await ProductService.update_product(id, payload, session)
        return IResponse(code=200, message="Product updated", data=new_product)
