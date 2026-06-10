from ollama import chat


def resposta_chat():
    mensagem =  input('Digite sua pergunta: ')
    print(mensagem)
    resposta = chat(
        model = 'llama3',
        messages =[
            {
                'role': 'user',
                'content': mensagem
            }
        ]
    )
    print('Consultando IA')
    print(resposta.message.content)
resposta_chat()
    
