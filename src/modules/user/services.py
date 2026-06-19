from sqlalchemy import delete, select, update

from src.core.database import SessionDep
from src.modules.user.model import User
from src.modules.user.schemas import UserCreate, UserPatch, UserResponse
from src.modules.auth.services import AuthService


class UserService:
    @staticmethod
    async def get_all(session: SessionDep):
        users = await session.execute(select(User))
        users_orm = users.scalars().all()
        return [UserResponse.model_validate(us) for us in users_orm]

    @staticmethod
    async def get_by_id(id: int, session: SessionDep):
        user = await session.execute(select(User).where(User.id == id))
        user_orm = user.scalar_one_or_none()
        return None if not user else UserResponse.model_validate(user_orm)

    @staticmethod
    async def create_user(payload: UserCreate, session: SessionDep):
        try:
            payload.password = AuthService.hash_password(payload.password)
            user = User(**payload.model_dump())
            session.add(user)
            await session.commit()
            return UserResponse.model_validate(user)
        except:
            await session.rollback()
            raise

    @staticmethod
    async def update_user(id: int, payload: UserPatch, session: SessionDep):
        try:
            user = await session.execute(
                update(User)
                .where(User.id == id)
                .values(**payload.model_dump())
                .returning(User)
            )
            user_orm = user.scalar_one()
            await session.commit()
            return UserResponse.model_validate(user_orm)
        except:
            await session.rollback()
            raise

    @staticmethod
    async def delete_user(id: int, session: SessionDep):
        try:
            await session.execute(delete(User).where(User.id == id))
            await session.commit()
        except:
            await session.rollback()
            raise

    @staticmethod
    async def authenticate(email: str, password: str, session: SessionDep):
        user = await session.execute(
            select(User).where(
                User.email == email
                and User.password == AuthService.hash_password(password)
            )
        )
        user_orm = user.scalar_one_or_none()
        if not user_orm:
            return None
        return UserResponse.model_validate(user_orm)
