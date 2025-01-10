import traceback

from fastapi import Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from src.core.logging_utils import get_logger

logger = get_logger(__name__)


class ErrorResponse(BaseModel):
    code: str
    message: str

    def __init__(self, code: str, message: str):
        super().__init__(code=code, message=message)


class BadRequestError(Exception):
    status_code: int = 400
    code: str

    def __init__(self, code: str, message: str):
        self.code = "UNKNOWN" if not code else code.upper()
        self.message = message
        super().__init__(self.message)


class UnauthorizedError(Exception):
    status_code: int = 401
    code: str

    def __init__(self, code: str, message: str):
        self.code = code.upper()
        self.message = message
        super().__init__(self.message)


class ForbiddenError(Exception):
    status_code: int = 403
    code: str

    def __init__(self, code: str, message: str):
        self.code = code.upper()
        self.message = message
        super().__init__(self.message)


class NotFoundError(Exception):
    status_code: int = 404
    code: str

    def __init__(self, code: str, message: str):
        self.code = code.upper()
        self.message = message
        super().__init__(self.message)


class InternalServerError(Exception):
    status_code: int = 500
    code: str

    def __init__(self, code: str, message: str):
        self.code = code.upper()
        self.message = message
        super().__init__(self.message)


async def respond_bad_request(exception: BadRequestError):
    return JSONResponse(
        status_code=400,
        content=ErrorResponse(code=exception.code, message=exception.message).dict()
    )


async def unauthorized_exception_handler(request: Request, exc: UnauthorizedError):
    return JSONResponse(
        status_code=exc.status_code,
        content=ErrorResponse(code=exc.code, message=exc.message).dict()
    )


async def respond_unauthorized(exception: UnauthorizedError):
    return JSONResponse(
        status_code=401,
        content={"code": exception.code, "message": exception.message}
    )


async def respond_method_not_allowed():
    return JSONResponse(
        status_code=405,
        content={"code": "METHOD_NOT_ALLOWED", "message": "Method is not allowed."}
    )


async def forbidden_exception_handler(request: Request, exc: ForbiddenError):
    return JSONResponse(
        status_code=exc.status_code,
        content=ErrorResponse(code=exc.code, message=exc.message).dict()
    )


async def bad_request_exception_handler(request: Request, exc: BadRequestError):
    return JSONResponse(
        status_code=exc.status_code,
        content=ErrorResponse(code=exc.code, message=exc.message).dict()
    )


async def not_found_exception_handler(request: Request, exc: NotFoundError):
    return JSONResponse(
        status_code=exc.status_code,
        content=ErrorResponse(code=exc.code, message=exc.message).dict()
    )


async def internal_server_exception_handler(request: Request, exc: Exception):
    logger.error(f"Internal server error has occurred. error: {exc}")
    traceback.print_exc()
    return await respond_internal_server_error("Internal server error has occurred.")


async def respond_internal_server_error(message: str):
    return JSONResponse(
        status_code=500,
        content=ErrorResponse(code="INTERNAL_SEVER_ERROR", message=message).dict()
    )
