import redis

from src.core.file_utils import get_env_values


def create_connection_pool_for_redis():
    redis_host, redis_port = get_env_values("REDIS_HOST", "REDIS_PORT")

    return redis.ConnectionPool(
        host=redis_host,
        port=redis_port,
    )


def close_connection_for_redis():
    if redis_connection_pool is not None:
        redis_connection_pool.close()


async def get_connection_for_redis():
    if redis_connection_pool is None:
        return create_connection_pool_for_redis()

    return redis.Redis(connection_pool=redis_connection_pool)


redis_connection_pool = create_connection_pool_for_redis()
