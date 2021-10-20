from sqlalchemy.orm import Session
from sqlalchemy import select, func
from sqlalchemy.sql.elements import BooleanClauseList
from app.dependencies.database import Base
from app.models import ComexModel, Sh2Model, ViaModel


def unique(db: Session, model: Base, col):
    statement = select([func.distinct(col)]).select_from(select(model)).order_by(col)
    results = db.execute(statement)
    return results.scalars().all()


def get(
    db: Session, model: Base, columns_filter: BooleanClauseList, page: int, size: int
):
    statement = select(model)
    statement = statement.where(columns_filter)

    total = db.execute(select([func.count()]).select_from(statement)).scalar()
    statement = statement.offset((page - 1) * size).limit(size)
    results = db.execute(statement)
    results = results.scalars().all()
    return total, results


def get_comex(
    db: Session, model: Base, columns_filter: BooleanClauseList, page: int, size: int
):
    statement = select(model, Sh2Model, ViaModel).join(
        Sh2Model, Sh2Model.CO_NCM == ComexModel.COD_NCM
    ).join(
        ViaModel, ViaModel.CO_VIA == ComexModel.COD_VIA
    )
    statement = statement.where(columns_filter)

    total = db.execute(select([func.count()]).select_from(statement)).scalar()
    statement = statement.offset((page - 1) * size).limit(size)
    results = db.execute(statement)
    results = results.all()
    return total, [r[0].__dict__ | r[1].__dict__ | r[2].__dict__ for r in results]
