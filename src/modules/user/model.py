from src.core.database import Base
from sqlalchemy.orm import Mapped, mapped_column


class User(Base):
    __tablename__ = "users"
    id : Mapped[int] = mapped_column(primary_key=True)
    name : Mapped[str] = mapped_column()
    last_name : Mapped[str] = mapped_column(index=True)
    old : Mapped[int] = mapped_column()