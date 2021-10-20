from sqlalchemy import Column, Integer, String

from app.dependencies.database import Base


class Sh2Model(Base):
    __tablename__ = 'd_sh2'

    id = Column(Integer, primary_key=True)
    CO_SH2 = Column(Integer)
    NO_SH2_POR = Column(String)
    CO_NCM = Column(Integer)
    NO_NCM_POR = Column(String)


class ViaModel(Base):
    __tablename__ = 'd_via'

    id = Column(Integer, primary_key=True)
    CO_VIA = Column(Integer)
    NO_VIA = Column(String)


class ComexModel(Base):
    __tablename__ = 'f_comex'

    id = Column(Integer, primary_key=True)
    ANO = Column(Integer)
    MES = Column(Integer)
    COD_NCM = Column(Integer)
    COD_UNIDADE = Column(Integer)
    COD_PAIS = Column(Integer)
    SG_UF = Column(String)
    COD_VIA = Column(Integer)
    COD_URF = Column(Integer)
    VL_QUANTIDADE = Column(Integer)
    VL_PESO_KG = Column(Integer)
    VL_FOB = Column(Integer)
    MOVIMENTACAO = Column(String)
