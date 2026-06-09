from fastapi import FastAPI, Depends, HTTPException # importa a fastapi e as dependencias
from sqlalchemy.orm import Session #conectividade com banco de dados
import schemas, models, database #importa os arquivos
from database import engine, SessionLocal #engine responsavel pela conexão com o banco de dados, e sessionLocal é a fabrica de sessões
from models import Produto #importa o modelo
from typing import List

# Cria a aplicação
app = FastAPI()

# Criando a conexão com o banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# rota para listar produtos GET
@app.get('/produtos/', response_model= List[schemas.ProdutoResponse])
def listar_produtos(db: Session = Depends(get_db)):
    produtos = db.query(models.Produto).all()
    return produtos

# Criando a tabela no PostgreSQL
database.Base.metadata.create_all(bind=engine)

# Rota para criar tarefas POST
@app.post('/produtos/', response_model= schemas.ProdutoResponse)
def criar_produto(produto: schemas.ProdutoCreate, db: Session = Depends(get_db)):
    produto_criado = models.Produto(nome = produto.nome, quantidade = produto.quantidade, valor = produto.valor, descricao = produto.descricao)
    db.add(produto_criado)
    db.commit()
    db.refresh(produto_criado)
    return produto_criado


# Rota para achar um produto especifico
@app.get('/produtos/{id}', response_model= schemas.ProdutoResponse)
def encontrar_produto(id: int, db: Session = Depends(get_db)):
    encontrar = db.query(models.Produto).filter(models.Produto.id == id).first()
    if not encontrar:
        raise HTTPException(
            status_code= 404,
            detail= 'Produto não encontrado'     
        )
    return encontrar

# Rota para atualizar o produto
@app.put('/produtos/{id}',  response_model=schemas.ProdutoResponse)
def atualizar_produto(id: int, produto: schemas.ProdutoCreate, db: Session = Depends(get_db)):
    atualizar = db.query(models.Produto).filter(models.Produto.id == id).first()
    if not atualizar:
        raise HTTPException(
            status_code=404,
            detail= 'Produto não encontrado'
        )
    atualizar.nome = produto.nome
    atualizar.quantidade = produto.quantidade
    atualizar.valor = produto.valor
    atualizar.descricao = produto.descricao
    
    db.commit()
    db.refresh(atualizar)
    return atualizar




@app.delete('/produtos/{id}')
def deletar_produto(id:int, db: Session = Depends(get_db)):
    excluir = db.query(models.Produto).filter(models.Produto.id ==id).first()
    if not excluir:
        raise HTTPException(
            status_code=404,
            detail='Produto não encontrado'
        )
    db.delete(excluir)
    db.commit()
    return {'message': 'Produto excluido com sucesso'}


  