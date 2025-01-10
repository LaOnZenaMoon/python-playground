from typing import Any

from fastapi.responses import JSONResponse
from pydantic import BaseModel


async def respond_ok(data):
    return JSONResponse(
        status_code=200,
        content=OkResponse(data).dict()
    )


class OkResponse(BaseModel):
    code: str = "OK"
    data: Any = None

    def __init__(self, data):
        super().__init__(data=data)


async def respond_created(data):
    return JSONResponse(
        status_code=201,
        content=CreatedResponse(data).dict()
    )


class CreatedResponse(BaseModel):
    code: str = "CREATED"
    data: Any = None

    def __init__(self, data):
        super().__init__(data=data)
