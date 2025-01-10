from src.core.persistence import ping_on_mysql, ping_on_redis
from src.schemas import respond_ok


async def health_check():
    await ping_on_mysql()
    await ping_on_redis()
    return await respond_ok({})
