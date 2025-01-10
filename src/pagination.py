from dataclasses import dataclass
from math import ceil

from fastapi.responses import JSONResponse
from sqlalchemy import asc, desc

from src.core.constants import PARAMETERS_INVALID
from src.exceptions import BadRequestError
from src.schemas import OkResponse


@dataclass
class OffsetPageQueryParameters:
    MAX_PAGE_SIZE = 1000

    page_number: int
    page_size: int
    page_sort: str

    def __post_init__(self):
        self.page_number = max(self.page_number or 1, 1)
        self.page_size = max(self.page_size or 10, 1)
        self._converted_page_sort = OffsetPageQueryParameters._convert_page_sort(self.page_sort)
        self.check_page_size()

    def check_page_size(self):
        if self.page_size > self.MAX_PAGE_SIZE:
            raise BadRequestError(PARAMETERS_INVALID, f"Page size cannot exceed {self.MAX_PAGE_SIZE}")

    @staticmethod
    def _convert_page_sort(page_sort):
        if not page_sort:
            return []

        output = []
        for page_sort_element in page_sort.split(","):
            sort_field, sort_direction = page_sort_element.split(":")
            if not sort_field or not sort_direction:
                raise BadRequestError(PARAMETERS_INVALID, "Sort field and direction cannot be empty")

            sort_field = sort_field.strip()
            sort_direction = sort_direction.strip().lower()

            if sort_direction not in ["asc", "desc"]:
                raise BadRequestError(PARAMETERS_INVALID, "Sort direction must be either 'asc' or 'desc'")

            output.append((sort_field, sort_direction))

        return output

    def get_order_by(self):
        output = []
        for sort_field, sort_direction in self._converted_page_sort:
            if sort_direction == "asc":
                output.append(asc(sort_field))
            elif sort_direction == "desc":
                output.append(desc(sort_field))
        return output

    def get_offset(self):
        return (self.page_number - 1) * self.page_size


class PageResult:
    def __init__(self, elements, page_number, page_size, total_elements):
        self.elements = elements
        self.page_number = page_number
        self.page_size = page_size
        self.total_elements = total_elements


class OffsetPageResponse:
    def __init__(self, page_result: PageResult):
        assert page_result.elements is not None, "Contents cannot be None"

        self.page_size = page_result.page_size
        self.page_number = page_result.page_number
        self.number_of_elements = len(page_result.elements)
        self.total_elements = page_result.total_elements
        self.total_pages = ceil(page_result.total_elements / page_result.page_size)
        self.contents = page_result.elements


async def respond_pagination(data: OffsetPageResponse):
    return JSONResponse(
        status_code=200,
        content=OkResponse(data.__dict__).dict()
    )
