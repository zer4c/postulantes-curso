from sqlalchemy.orm import Mapped, mapped_column

from src.core.database import Base


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(index=True, unique=True)
    password: Mapped[str] = mapped_column()
    name: Mapped[str] = mapped_column()
    last_name: Mapped[str] = mapped_column(index=True)
    old: Mapped[int] = mapped_column()
