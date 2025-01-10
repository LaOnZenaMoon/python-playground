from datetime import datetime
from zoneinfo import ZoneInfo


async def case_insensitive_contains(source: str, target: str) -> bool:
    if not source or not target:
        return False

    return target.lower() in source.lower()


def current_date_time() -> datetime:
    return datetime.now(ZoneInfo("Asia/Seoul"))
