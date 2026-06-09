from sqlalchemy import create_engine #ligação entre a aplicação e o banco de dados python -> engine -> postgreSQL
from sqlalchemy.orm import sessionmaker, declarative_base # sessionmaker executa o CRUD, declarative_base é a mãe de todas as tabelas

DATABASE_URL = 'postgresql://postgres:lucas0612@localhost/controle_estoque' #URL do banco de dados

engine = create_engine(DATABASE_URL) #cria a engine, faz todas as conexões

SessionLocal = sessionmaker(
    autocommit=False, # nada será salvo automaticamente, evita erros 
    autoflush=False, #evita alterações pendentes para o banco
    bind=engine #sessão mostra qual deve usar

)

Base = declarative_base() # está variavel cria a base para todas as tabelas