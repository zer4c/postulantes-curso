from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlalchemy import text

import src.core.mapping_database  # noqa
from src.core.api import api
from src.core.database import create_database, engine


@asynccontextmanager
async def lifespan(_app: FastAPI):
    try:
        async with engine.connect() as conn:
            await conn.execute(text("SELECT 1"))
            await create_database()
    except Exception as e:
        print(e)
    yield
    print("servidor cerrado")


app = FastAPI(lifespan=lifespan)

app.include_router(api)
