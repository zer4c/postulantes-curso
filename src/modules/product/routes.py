from fastapi import APIRouter, status
from src.modules.product.controller import ProductController
from src.core.database import SessionDep
from src.modules.product.schemas import ProductCreate, ProductPatch
from src.core.response_model import IResponse

router = APIRouter()


@router.get("/", status_code=200, response_model=IResponse)
async def get_all_product(session: SessionDep, limit : int = 2, offset : int = 0):
    return await ProductController.get_all_products(session, limit , offset)


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=IResponse)
async def get_by_id(id: int, session: SessionDep):
    return await ProductController.get_by_id(id, session)


@router.post("/", status_code=201, response_model=IResponse)
async def create_product(session: SessionDep, payload: ProductCreate):
    return await ProductController.create_product(payload, session)

@router.delete("/{id}", status_code=204)
async def delete_product(session : SessionDep, id : int):
    await ProductController.delete_product(id, session)

@router.patch("/{id}", status_code=status.HTTP_200_OK, response_model=IResponse)
async def patch_product(session : SessionDep, id : int, payload: ProductPatch):
    return await ProductController.update_product(id, payload, session)