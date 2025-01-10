from fastapi import APIRouter

from src.core.http_utils import get_responses
from src.core.service import health_check as health_check_in_service

router = APIRouter()


@router.get("/health-check", responses=get_responses(), tags=["Core"])
async def health_check():
    return await health_check_in_service()
