"""

4 - Crie um programa que leia e escreva arquivos no formato JSON, que salve em um dicionário com nome, idade e cidade em um arquivo JSON e depois leia o mesmo arquivo exibindo os dados, caso o arquivo não existir ou ocorrer erro ao salvar, mostre uma mensagem de falha. 

"""

import json

def salvar_dados_json(caminho_arquivo, dados):
  if not caminho_arquivo.endswith('.json'):
    caminho_arquivo += '.json'
  try:
    with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo_json:
      json.dump(dados, arquivo_json, ensure_ascii=False, indent=4)
    print(f"Arquivo '{caminho_arquivo}' salvo com sucesso.")
    return caminho_arquivo
  except Exception as e:
    print(f"Falha ao salvar o arquivo: {e}")
    return None

def ler_dados_json(caminho_arquivo):
  try:
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo_json:
      dados = json.load(arquivo_json)
      print("Dados lidos do arquivo JSON:")
      print(dados)
  except FileNotFoundError:
    print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
  except Exception as e:
    print(f"Falha ao ler o arquivo: {e}")

dados = {
  "nome": "Ana",
  "idade": 30,
  "cidade": "Rio de Janeiro"
}

caminho_arquivo = input("Digite o nome do arquivo JSON para salvar os dados (ex: pessoas.json): ")

caminho_arquivo = salvar_dados_json(caminho_arquivo, dados)

if caminho_arquivo:
  ler_dados_json(caminho_arquivo)