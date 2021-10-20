from fastapi.params import Query
from fastapi_pagination import Params as PageParams


def page_params(
    page: int = Query(1, ge=1, description="Page number"),
    size: int = Query(50, ge=1, le=100, description="Page size")
):
    return PageParams(page=page, size=size)


def page_results(items, total, page, size):
    return {
        'items': items,
        'total': total,
        'page': page,
        'size': size
    }
