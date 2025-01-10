import time
from enum import Enum

from aiohttp.hdrs import AUTHORIZATION
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

from src.core.constants import APP_ENV_LOCAL
from src.core.file_utils import get_app_env, get_app_name
from src.core.logging_utils import get_logger
from src.exceptions import ErrorResponse
from src.schemas import OkResponse

logger = get_logger(__name__)


async def get_header_value(request: Request, header_key: str):
    return request.headers.get(header_key)


async def get_authorization_value(request: Request):
    authorization = await get_header_value(request, AUTHORIZATION)

    if authorization is None:
        return None

    return authorization.replace("Bearer ", "")


def get_enum_examples(codes: Enum):
    return " [" + ", ".join([f'"{code.value}"' for code in codes]) + "]"


def get_responses():
    return {
        200: {
            "model": OkResponse
        },
        201: {
            "model": OkResponse
        },
        400: {
            "model": ErrorResponse,
        },
        401: {
            "model": ErrorResponse,
        },
        403: {
            "model": ErrorResponse,
        },
        404: {
            "model": ErrorResponse,
        },
        405: {
            "model": ErrorResponse,
        },
        422: {
            "model": ErrorResponse,
        },
        500: {
            "model": ErrorResponse,
        }
    }


class LoggingMiddleware(BaseHTTPMiddleware):
    exception_cases = ["/health-check"]

    async def dispatch(self, request: Request, call_next):
        if request.url.path in self.exception_cases:
            return await call_next(request)

        start_time = time.time()
        response = await call_next(request)
        end_time = time.time()

        api_key = await get_authorization_value(request)

        if api_key:
            logger.info(
                f"{request.method} {request.url} {response.status_code} {end_time - start_time:.3f} sec, Authorization: Bearer {api_key}")
        else:
            logger.info(f"{request.method} {request.url} {response.status_code} {end_time - start_time:.3f} sec")

        return response


def get_openapi_servers():
    pass


def get_swagger_docs_url():
    app_env = get_app_env()

    if app_env == APP_ENV_LOCAL:
        return "/docs"

    return "/swagger.html"


def get_openapi_prefix():
    app_env = get_app_env()

    if app_env == APP_ENV_LOCAL:
        return

    app_name = get_app_name()
    return f"/{app_name}/docs"
