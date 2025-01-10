from sqlalchemy import text

from src.database import get_connection_for_db
from src.memory_database import get_connection_for_redis


async def ping_on_mysql():
    async with get_connection_for_db() as db:
        await db.execute(text("select 1;"))


async def ping_on_redis():
    redis = await get_connection_for_redis()
    redis.ping()
