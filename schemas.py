from pydantic import BaseModel

class ProdutoCreate(BaseModel):
    nome: str
    quantidade: int
    valor: float
    descricao: str

class ProdutoResponse(BaseModel):
    id: int
    nome: str
    quantidade: int
    valor: float
    descricao: str

class PerguntaIA(BaseModel):
    pergunta: str

class RespostaIA(BaseModel):
    resposta: str

    class Config: #classe para que o pydantic leia os atributos dos objetos ORM
        from_attributes=True