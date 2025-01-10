from http import HTTPMethod

from aiohttp.hdrs import AUTHORIZATION
from fastapi import Request, APIRouter
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from starlette.authentication import (
    AuthenticationBackend, SimpleUser, AuthCredentials
)
from starlette.middleware.base import BaseHTTPMiddleware

from src.core.constants import AUTHENTICATION_INVALID
from src.core.logging_utils import get_logger
from src.exceptions import respond_unauthorized, UnauthorizedError, respond_method_not_allowed

router = APIRouter()
logger = get_logger(__name__)


class CustomAuthenticationBackend(AuthenticationBackend):
    async def authenticate(self, request):
        if AUTHORIZATION in request.headers:
            credentials: HTTPAuthorizationCredentials = await HTTPBearer().__call__(request)
            return AuthCredentials(["authenticated"]), SimpleUser(credentials.credentials)

        await self.raise_authentication_error()

    async def raise_authentication_error(self):
        raise UnauthorizedError(AUTHENTICATION_INVALID, "Authentication is invalid.")


class AuthenticationMiddleware(BaseHTTPMiddleware):
    authentication_exception_cases = {
        "/docs": [HTTPMethod.GET],
        "/swagger.html": [HTTPMethod.GET],
        "/openapi.json": [HTTPMethod.GET],
        "/redoc": [HTTPMethod.GET],
        "/health-check": [HTTPMethod.GET],
        "/news": [HTTPMethod.POST],
    }

    async def dispatch(self, request: Request, call_next):
        for url_path, methods in self.authentication_exception_cases.items():
            if request.url.path.startswith(url_path):
                if request.method not in methods:
                    return await respond_method_not_allowed()
                return await call_next(request)

        try:
            auth_backend = CustomAuthenticationBackend()
            await auth_backend.authenticate(request)
        except UnauthorizedError as uae:
            return await respond_unauthorized(uae)

        response = await call_next(request)
        return response
