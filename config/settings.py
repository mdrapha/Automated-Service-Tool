import json
import pandas as pd


class Settings:
    def __init__(self, config_file="data.json"):
        self.whatsapp_number = None
        self.openai_key = None
        self.company_name = None
        self.company_category = None
        self.company_founded = None
        self.company_address = None
        self.load_config(config_file)

    def load_config(self, config_file):
        with open(config_file, "r") as file:
            data = json.load(file)
            self.whatsapp_number = "+5512996597939"
            self.openai_key = None
            self.company_name = "Protech"
            self.company_category = "Loja de Eletrônicos"
            self.company_founded = "2019"
            self.company_address = "Rua João Pessoa, 1000"


open("data2.json", "w").write("oi")
test = Settings("data2.json")

print(test.whatsapp_number)
