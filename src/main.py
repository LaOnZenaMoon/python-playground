from aiohttp.hdrs import AUTHORIZATION
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from starlette.middleware.cors import CORSMiddleware

from src.config import AuthenticationMiddleware
from src.core.file_utils import get_app_name
from src.core.http_utils import LoggingMiddleware, get_openapi_servers
from src.core.router import router as core_router
from src.database import database
from src.exceptions import BadRequestError, bad_request_exception_handler, UnauthorizedError, \
    unauthorized_exception_handler, ForbiddenError, forbidden_exception_handler, NotFoundError, \
    not_found_exception_handler, internal_server_exception_handler

app = FastAPI()

app.add_exception_handler(BadRequestError, bad_request_exception_handler)
app.add_exception_handler(UnauthorizedError, unauthorized_exception_handler)
app.add_exception_handler(ForbiddenError, forbidden_exception_handler)
app.add_exception_handler(NotFoundError, not_found_exception_handler)
app.add_exception_handler(Exception, internal_server_exception_handler)
app.include_router(core_router)
app.add_middleware(LoggingMiddleware)
app.add_middleware(AuthenticationMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("shutdown")
async def shutdown():
    await database.engine.dispose()


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=get_app_name(),
        version="1.0.0",
        description="Playground for python",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        AUTHORIZATION: {
            "type": "http",
            "scheme": "bearer",
        },
    }
    openapi_schema["security"] = [{AUTHORIZATION: []}]
    openapi_schema["servers"] = get_openapi_servers()
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
