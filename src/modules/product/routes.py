from fastapi import APIRouter, status
from src.modules.product.controller import ProductController
from src.core.database import SessionDep
from src.modules.product.schemas import ProductResponse, ProductCreate

router = APIRouter()


@router.get("/", status_code=200, response_model=list[ProductResponse])
async def get_all_product(session: SessionDep):
    return await ProductController.get_all_products(session)


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=ProductResponse)
async def get_by_id(id: int, session: SessionDep):
    return await ProductController.get_by_id(id, session)


@router.post("/", status_code=201, response_model=ProductResponse)
async def create_product(session: SessionDep, payload: ProductCreate):
    return await ProductController.create_product(payload, session)
