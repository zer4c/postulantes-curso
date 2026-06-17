from src.core.database import SessionDep
from sqlalchemy import select, delete, update
from src.modules.product.model import Product
from src.modules.product.schemas import ProductResponse, ProductCreate, ProductPatch


class ProductService:
    @staticmethod
    async def create_product(payload: ProductCreate, session: SessionDep):
        product = Product(
            name=payload.name,
            price=payload.price,
            category_product=payload.category_product,
        )
        session.add(product)
        await session.commit()
        return ProductResponse.model_validate(product)

    @staticmethod
    async def get_by_id(id: int, session: SessionDep):
        product = await session.execute(select(Product).where(Product.id == id))
        product_orm = product.scalar_one_or_none()
        if not product_orm:
            return None
        return ProductResponse.model_validate(product_orm)

    @staticmethod
    async def get_all_products(session: SessionDep, limit, offset):
        product_list = await session.execute(
            select(Product).limit(limit).offset(offset)
        )
        product_list_orm = product_list.scalars().all()
        return [ProductResponse.model_validate(product) for product in product_list_orm]

    @staticmethod
    async def delete_product(id: int, session: SessionDep):
        await session.execute(delete(Product).where(Product.id == id))
        await session.commit()

    @staticmethod
    async def update_product(id: int, payload: ProductPatch, session: SessionDep):
        product = await session.execute(
            update(Product)
            .where(Product.id == id)
            .values(**payload.model_dump(exclude_unset=True))
            .returning(Product)
        )
        product_orm = product.scalar_one()
        return ProductResponse.model_validate(product_orm)
