"""

2 - Crie um programa que cria um arquivo CSV com nome, idade e cidade de algumas pessoas, que este programa escreva os dados em formato tabular e salva no arquivo escolhido pelo usuário, caso ocorra um erro ao salvar, mostre uma mensagem de falha. 

"""

import csv

def criar_arquivo_csv(caminho_arquivo, dados):
  if not caminho_arquivo.endswith('.csv'):
    caminho_arquivo += '.csv'
  try:
    with open(caminho_arquivo, 'w', newline='', encoding='utf-8') as arquivo:
      writer = csv.writer(arquivo)
      writer.writerow(['Nome', 'Idade', 'Cidade'])
      writer.writerows(dados)
    print(f"Arquivo '{caminho_arquivo}' salvo com sucesso.")
  except Exception as e:
    print(f"Falha ao salvar o arquivo: {e}")

dados = [
  ['Rodrigo', 28, 'São Paulo'],
  ['Maria', 34, 'Brasília'],
  ['Pedro', 22, 'Manaus'],
]
caminho_arquivo = input("Digite o nome do arquivo CSV para salvar os dados (ex: pessoas.csv): ")

criar_arquivo_csv(caminho_arquivo, dados)