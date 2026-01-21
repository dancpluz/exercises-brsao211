"""

1 - Crie um programa que gere senhas aleatórias com letras, números e símbolos e que o usuário  também escolha o tamanho da senha para criar senhas seguras automaticamente.

"""

import random
import string

def gerar_senha(tamanho):
  caracteres = string.ascii_letters + string.digits + string.punctuation
  senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
  return senha

while True:
  try:
    tamanho_senha = int(input("\nDigite o tamanho da senha desejada: "))
    senha_gerada = gerar_senha(tamanho_senha)
    print("Senha gerada:", senha_gerada)
  except ValueError:
    print("Por favor, insira um número válido para o tamanho da senha.")