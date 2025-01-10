import asyncio
from contextlib import asynccontextmanager

from sqlalchemy import URL, desc
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, async_scoped_session

from src.core import constants
from src.core.constants import APP_ENV_LOCAL
from src.core.file_utils import get_env_values, get_app_env
from src.exceptions import InternalServerError, NotFoundError, BadRequestError
from src.pagination import OffsetPageQueryParameters

driver_name, host, port, database, username, password = get_env_values("DB_DRIVER_NAME", "DB_HOST", "DB_PORT",
                                                                       "DB_DATABASE", "DB_USERNAME", "DB_PASSWORD")

datasource_url = URL.create(
    drivername=driver_name,
    host=host,
    port=port,
    database=database,
    username=username,
    password=password,
)

echo = True if get_app_env() == APP_ENV_LOCAL else False
engine = create_async_engine(datasource_url, echo=echo, pool_size=10, max_overflow=20)
session_maker = async_sessionmaker(autocommit=False, autoflush=False, bind=engine)
created_scoped_session = async_scoped_session(session_maker, scopefunc=asyncio.current_task)


@asynccontextmanager
async def get_connection_for_db():
    session = created_scoped_session()

    try:
        yield session
    except (BadRequestError, NotFoundError) as e:
        await session.rollback()
        raise e
    except Exception as e:
        await session.rollback()
        raise InternalServerError(constants.INTERNAL_SERVER_ERROR, e)
    finally:
        await session.close()


async def get_order_by(request: OffsetPageQueryParameters, model, field):
    return request.get_order_by() if request.get_order_by() else [desc(getattr(model, field))]
