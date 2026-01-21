"""

3 - Crie um programa que leia um arquivo CSV informado pelo usuário, percorrendo cada linha do arquivo e a exibe na tela, caso o arquivo não seja encontrado, mostre uma mensagem de erro.

"""

import csv

def ler_arquivo_csv(nome_arquivo):
  try:
    with open(nome_arquivo, mode='r', newline='', encoding='utf-8') as arquivo_csv:
      leitor_csv = csv.reader(arquivo_csv)
      for linha in leitor_csv:
        print(linha)
  except FileNotFoundError:
    print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")

nome_arquivo = input("Digite o nome do arquivo CSV para ler os dados (ex: pessoas.csv): ")
ler_arquivo_csv(nome_arquivo)