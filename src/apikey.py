import os


def get_key():  # Função para obter a API key
    try:
        with open(r"\Users\Raphael\Desktop\key_openai.txt", "r") as file:
            api_key = file.read().strip()
            return api_key
    except FileNotFoundError:
        print("Arquivo de Key não encontrado.")
        return None
    except Exception as e:
        print("Erro ao ler a API key:", e)
        return None
