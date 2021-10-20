from typing import List
from fastapi import APIRouter, Depends
from fastapi.param_functions import Query
from sqlalchemy.orm import Session
from sqlalchemy.sql.elements import BooleanClauseList
from sqlalchemy.sql.expression import column as c
from app import schemas
from app.dependencies.database import get_db
from fastapi_pagination import Page
from app.dependencies.pagination import PageParams, page_params, page_results
from app.crud import crud, filters
from app.models import Sh2Model

router = APIRouter(
    prefix='/d_sh2',
    tags=['d_sh2'],
)


@router.get(
    '/column-values',
    response_model=List[str]
)
async def get_distinct(
    column: schemas.ColumnsSh2 = Query(..., description='nome da coluna'),
    db: Session = Depends(get_db)
):
    return crud.unique(db, Sh2Model, c(column.value))


@router.get('/', response_model=Page[schemas.Sh2Schema])
def get_sh2(
    columns_filter: BooleanClauseList = Depends(filters.sh2),
    pagination: PageParams = Depends(page_params),
    db: Session = Depends(get_db)
):
    page = pagination.page
    size = pagination.size
    total, items = crud.get(db, Sh2Model, columns_filter, page, size)
    return page_results(items, total, page, size)
