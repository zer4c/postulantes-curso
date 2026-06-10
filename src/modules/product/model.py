from src.core.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Enum
from src.core.enums import TypeProduct

class Product(Base):
    __tablename__ = "products"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(index=True)
    price: Mapped[int] = mapped_column()
    category_product : Mapped[TypeProduct] = mapped_column(Enum(TypeProduct))
    
    
