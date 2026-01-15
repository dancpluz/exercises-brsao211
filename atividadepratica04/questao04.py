"""

4 - Criar um código que serve para analisar números digitados pelo usuário, classificando-os como pares ou ímpares e contabilizando quantos de cada tipo foram inseridos.

"""

pares = 0
impares = 0

while True:
  entrada_numero = input("\nDigite um número inteiro (ou 'sair' para encerrar): ")
  if entrada_numero.lower() == 'sair':
    break
  try:
    numero = int(entrada_numero)
    if numero % 2 == 0:
      pares += 1
      print(f"O número {numero} é par.")
    else:
      impares += 1
      print(f"O número {numero} é ímpar.")
  except ValueError:
    print("Entrada inválida. Por favor, insira um número inteiro ou 'sair'.")

print(f"\nTotal de números pares inseridos: {pares}")
print(f"Total de números ímpares inseridos: {impares}")