from src.core.database import SessionDep
from sqlalchemy import select
from src.modules.product.model import Product
from src.modules.product.schemas import ProductResponse, ProductCreate


class ProductService:
    @staticmethod
    async def create_product(payload : ProductCreate, session : SessionDep ):
        product = Product(
            name = payload.name,
            price = payload.price,
            category_product = payload.category_product
        )
        session.add(product)
        await session.commit()
        return ProductResponse.model_validate(product)

    @staticmethod
    async def get_by_id(id: int, session : SessionDep):
        product = await session.execute(
            select(Product).where(Product.id == id)
        )
        product_orm = product.scalar_one_or_none()
        if not product_orm:
            return None
        return ProductResponse.model_validate(product_orm)

    @staticmethod
    async def get_all_products(session: SessionDep):
        product_list = await session.execute(select(Product))
        product_list_orm = product_list.scalars().all()
        return [ProductResponse.model_validate(product) for product in product_list_orm]
