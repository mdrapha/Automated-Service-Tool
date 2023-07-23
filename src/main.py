import os
import openai
import apikey

openai.api_key = apikey.get_key()

if openai.api_key is None:
    print(
        "Não foi possível obter a API key. Por favor, verifique se o arquivo key_openai.txt está no diretório correto."
    )
    exit()

# Função para interagir com o modelo e obter a resposta do chatbot
def obter_resposta(mensagens):
    try:
        # Fazer uma chamada à API para obter a resposta do modelo GPT-3.5-turbo com as mensagens de entrada
        resposta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=mensagens,
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
        )
        content = resposta["choices"][0]["message"]["content"]
        return content

    except Exception as e:
        # Lidar com exceções se ocorrerem erros durante a interação com a API
        print("Erro na chamada da API:", e)
        return "Desculpe, ocorreu um erro ao processar sua solicitação. Por favor, tente novamente."


# Função principal para interagir com o cliente
def atendimento_ao_cliente():
    print("Bem-vindo à loja Protech! Como posso ajudá-lo hoje?")
    while True:
        pergunta = input("Você: ")

        # Finalizar a conversa se o usuário digitar 'sair'
        if pergunta.lower() == "sair":
            print("Obrigado por visitar a loja Protech. Tenha um ótimo dia!")
            break

        # Definir as mensagens para a API do ChatCompletion
        mensagens = [
            {
                "role": "system",
                "content": "Você é um assistente útil.",
            },  # Você é um assistente útil.
            {
                "role": "system",
                "content": "Você será o atendente de uma loja de eletrônicos (pode assumir que todos os itens existem e dar valores ficticios aos mesmos.) ",
            },
            {"role": "user", "content": pergunta},  # O cliente pergunta algo.
        ]

        # Obter a resposta do chatbot com base na pergunta do cliente
        resposta = obter_resposta(mensagens)

        print("Protech: " + str(resposta))


# Iniciar a interação com o cliente
if __name__ == "__main__":
    atendimento_ao_cliente()
