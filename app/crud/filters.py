from fastapi import Query
from sqlalchemy.sql.expression import and_
from app import models

from app.dependencies.config import ColValue


def sh2(
    co_sh2: int = Query(None, description='Valor da coluna CO_SH2'),
    no_sh2_por: str = Query(None, description='Valor da coluna NO_SH2_POR'),
    co_ncm: int = Query(None, description='Valor da coluna CO_NCM'),
    no_ncm_por: str = Query(None, description='Valor da coluna NO_NCM_POR'),
):
    consulta_eq = [
        ColValue(models.Sh2Model.CO_SH2, co_sh2),
        ColValue(models.Sh2Model.NO_SH2_POR, no_sh2_por),
        ColValue(models.Sh2Model.CO_NCM, co_ncm),
        ColValue(models.Sh2Model.NO_NCM_POR, no_ncm_por),
    ]
    consulta_eq = [*filter(lambda x: x.value is not None, consulta_eq)]
    return and_(
        *[x.column == x.value for x in consulta_eq]
    )


def via(
    co_via: int = Query(None, description='Valor da coluna CO_VIA'),
    no_via: str = Query(None, description='Valor da coluna NO_VIA')
):
    consulta_eq = [
        ColValue(models.ViaModel.CO_VIA, co_via),
        ColValue(models.ViaModel.NO_VIA, no_via)
    ]
    consulta_eq = [*filter(lambda x: x.value is not None, consulta_eq)]
    return and_(
        *[x.column == x.value for x in consulta_eq]
    )


def comex(
    ano: int = Query(None, description='Valor da coluna ANO'),
    mes: int = Query(None, description='Valor da coluna MES'),
    cod_ncm: int = Query(None, description='Valor da coluna COD_NCM'),
    cod_unidade: int = Query(None, description='Valor da coluna COD_UNIDADE'),
    cod_pais: int = Query(None, description='Valor da coluna COD_PAIS'),
    sg_uf: int = Query(None, description='Valor da coluna SG_UF'),
    cod_urf: int = Query(None, description='Valor da coluna COD_URF'),
    vl_quantidade: int = Query(None, description='Valor da coluna VL_QUANTIDADE'),
    vl_peso_kg: int = Query(None, description='Valor da coluna VL_PESO_KG'),
    vl_fob: int = Query(None, description='Valor da coluna VL_FOB'),
    movimentacao: str = Query(None, description='Valor da coluna MOVIMENTACAO'),
    no_sh2_por: str = Query(None, description='Valor da coluna NO_SH2_POR'),
    no_via: str = Query(None, description='Valor da coluna NO_VIA'),
):
    consulta_eq = [
        ColValue(models.ComexModel.ANO, ano),
        ColValue(models.ComexModel.MES, mes),
        ColValue(models.ComexModel.COD_NCM, cod_ncm),
        ColValue(models.ComexModel.COD_UNIDADE, cod_unidade),
        ColValue(models.ComexModel.COD_PAIS, cod_pais),
        ColValue(models.ComexModel.SG_UF, sg_uf),
        ColValue(models.ComexModel.COD_URF, cod_urf),
        ColValue(models.ComexModel.VL_QUANTIDADE, vl_quantidade),
        ColValue(models.ComexModel.VL_PESO_KG, vl_peso_kg),
        ColValue(models.ComexModel.VL_FOB, vl_fob),
        ColValue(models.ComexModel.MOVIMENTACAO, movimentacao),
        ColValue(models.Sh2Model.NO_SH2_POR, no_sh2_por),
        ColValue(models.ViaModel.NO_VIA, no_via),
    ]
    consulta_eq = [*filter(lambda x: x.value is not None, consulta_eq)]
    return and_(
        *[x.column == x.value for x in consulta_eq]
    )
