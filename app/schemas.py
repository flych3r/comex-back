from enum import Enum
from typing import Optional
from pydantic.main import BaseModel
from pydantic_sqlalchemy import sqlalchemy_to_pydantic
from app.models import Sh2Model, ViaModel


class ColumnsSh2(str, Enum):
    CO_SH2 = 'CO_SH2'
    NO_SH2_POR = 'NO_SH2_POR'
    CO_NCM = 'CO_NCM'
    NO_NCM_POR = 'NO_NCM_POR'


class ColumnsVia(str, Enum):
    CO_VIA = 'CO_VIA'
    NO_VIA = 'NO_VIA'


class ColumnsComex(str, Enum):
    ANO = 'ANO'
    MES = 'MES'
    COD_NCM = 'COD_NCM'
    COD_UNIDADE = 'COD_UNIDADE'
    COD_PAIS = 'COD_PAIS'
    SG_UF = 'SG_UF'
    COD_VIA = 'COD_VIA'
    COD_URF = 'COD_URF'
    VL_QUANTIDADE = 'VL_QUANTIDADE'
    VL_PESO_KG = 'VL_PESO_KG'
    VL_FOB = 'VL_FOB'
    MOVIMENTACAO = 'MOVIMENTACAO'


Sh2Schema = sqlalchemy_to_pydantic(Sh2Model, exclude=['id'])
ViaSchema = sqlalchemy_to_pydantic(ViaModel, exclude=['id'])


class ComexSchema(BaseModel):
    ANO: int
    MES: int
    COD_NCM: int
    COD_UNIDADE: int
    COD_PAIS: int
    SG_UF: str
    COD_VIA: int
    COD_URF: int
    VL_QUANTIDADE: int
    VL_PESO_KG: int
    VL_FOB: int
    MOVIMENTACAO: str
    NO_SH2_POR: Optional[str]
    NO_VIA: Optional[str]
