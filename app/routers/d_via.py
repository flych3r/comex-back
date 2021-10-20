from typing import List
from fastapi import APIRouter, Depends
from fastapi.param_functions import Query
from sqlalchemy.orm import Session
from sqlalchemy.sql.elements import BooleanClauseList
from app import schemas
from sqlalchemy.sql.expression import column as c
from app.dependencies.database import get_db
from fastapi_pagination import Page
from app.dependencies.pagination import PageParams, page_params, page_results
from app.crud import crud, filters
from app.models import ViaModel

router = APIRouter(
    prefix='/d_via',
    tags=['d_via'],
)


@router.get(
    '/column-values',
    response_model=List[str]
)
async def get_distinct(
    column: schemas.ColumnsVia = Query(..., description='nome da coluna'),
    db: Session = Depends(get_db)
):
    return crud.unique(db, ViaModel, c(column.value))


@router.get('/', response_model=Page[schemas.ViaSchema])
def get_via(
    columns_filter: BooleanClauseList = Depends(filters.via),
    pagination: PageParams = Depends(page_params),
    db: Session = Depends(get_db)
):
    page = pagination.page
    size = pagination.size
    total, items = crud.get(db, ViaModel, columns_filter, page, size)
    return page_results(items, total, page, size)
