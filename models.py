from database import Base # Puxa a base 
from sqlalchemy import Column, Integer, String, Float # Importa as propriedades do sql


class Produto(Base):
    __tablename__ = 'produtos'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    quantidade = Column(Integer)
    valor = Column(Float)
    descricao = Column(String)