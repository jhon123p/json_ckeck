import json

arquivo = '/dados.json'

print(arquivo)


with open('dados.json', 'r') as arquivo_json:
    dados = json.load(arquivo_json)
    
info_filter = [item for item in dados if item['categoria'] == 'Programação']

print(info_filter)