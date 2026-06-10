from ollama import chat
from pydantic import BaseModel

def perguntar_ia(pergunta):
    resposta  = chat(
        model = 'llama3',
        messages = [
            {
                'role':'user',
                'content': pergunta
            }
        ]
    )
    return resposta.message.content



