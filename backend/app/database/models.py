from sqlalchemy import Column, Float, Integer, String

from app.database.connection import Base


class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(120), nullable=False)
    categoria = Column(String(80), nullable=False)
    quantidade = Column(Integer, default=0)
    estoque_minimo = Column(Integer, default=5)
    custo = Column(Float, nullable=False)
    margem_lucro = Column(Float, default=30.0)
