import os
import openai

# import apikey


class ChatBot:
    def __init__(self, config=None):

        if config is None:
            config = {
                "name": "Protech",
                "salutation": "Bem-vindo à loja Protech! Como posso ajudá-lo hoje?",
                "farewell": "Obrigado por visitar a loja Protech. Tenha um ótimo dia!",
            }

        # Configurações da empresa para o chatbot
        self.name = config["name"]
        self.salutation = config["salutation"]
        self.farewell = config["farewell"]

    def apikey_load(self):
        try:
            with open(r"\Users\Raphael\Desktop\key_openai.txt", "r") as file:
                api_key = file.read().strip()
        except FileNotFoundError:
            print("Arquivo de Key não encontrado.")
        except Exception as e:
            print("Erro ao ler a API key:", e)

        openai.api_key = api_key

        if openai.api_key is None:
            print(
                "Não foi possível obter a API key. Por favor, verifique se o arquivo key_openai.txt está no diretório correto."
            )
            exit()

    # Função para interagir com o modelo e obter a resposta do chatbot
    def obter_resposta(self, messages):
        try:
            # Fazer uma chamada à API para obter a resposta do modelo GPT-3.5-turbo com as mensagens de entrada
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
                temperature=1,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0,
            )

            # TODO: Se algo der errado, analisar essa parte do código!
            return response.choices[0].message.content.strip()

        except Exception as e:
            # Lidar com exceções se ocorrerem erros durante a interação com a API
            print("Erro na chamada da API:", e)
            return "Desculpe, ocorreu um erro ao processar sua solicitação. Por favor, tente novamente."

    # Method to get response from the chatbot model
    def get_response(self, pergunta):
        messages = [
            {"role": "system", "content": "Você é um assistente útil."},
            {
                "role": "system",
                "content": "Você será o atendente de uma loja de eletrônicos (pode assumir que todos os itens existem e dar valores ficticios aos mesmos.)",
            },
            {"role": "user", "content": pergunta},
        ]

        try:
            # Fazer uma chamada à API para obter a resposta do modelo GPT-3.5-turbo com as mensagens de entrada
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
                temperature=1,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0,
            )

            # TODO: Se algo der errado, analisar essa parte do código!
            return response.choices[0].message.content.strip()

        except Exception as e:
            # Lidar com exceções se ocorrerem erros durante a interação com a API
            print("Erro na chamada da API:", e)
            return "Desculpe, ocorreu um erro ao processar sua solicitação. Por favor, tente novamente."

    # Função principal para interagir com o cliente
    def atendimento_ao_cliente(self):
        self.apikey_load()
        print("Bem-vindo à loja Protech! Como posso ajudá-lo hoje?")
        while True:
            pergunta = input("Você: ")

            # Finalizar a conversa se o usuário digitar 'sair'
            if pergunta.lower() == "sair":
                print("Obrigado por visitar a loja Protech. Tenha um ótimo dia!")
                break

            # Definir as mensagens para a API do ChatCompletion
            mensagens = [
                {"role": "system", "content": "Você é um assistente útil."},
                {
                    "role": "system",
                    "content": "Você será o atendente de uma loja de eletrônicos (pode assumir que todos os itens existem e dar valores ficticios aos mesmos.)",
                },
                {"role": "user", "content": pergunta},
            ]

            # Obter a resposta do chatbot com base na pergunta do cliente
            resposta = self.obter_resposta(mensagens)

            print("Protech: " + str(resposta))


# Iniciar a interação com o cliente
if __name__ == "__main__":
    ChatBot().atendimento_ao_cliente()
