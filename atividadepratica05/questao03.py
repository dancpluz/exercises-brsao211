"""

3 - Crie um programa que serve para calcular o preço final de um produto após aplicar um desconto percentual.
a - Cálculo de desconto: Calcula o valor do desconto baseado em uma porcentagem.
b - Preço final: Determina o novo preço após o desconto.
c - Formatação: Arredonda o resultado para 2 casas decimais (centavos).
d - Interação com usuário: Pede os valores necessários e mostra o resultado formatado.

"""

def calcular_desconto(preco_original, porcentagem_desconto):
  valor_desconto = preco_original * (porcentagem_desconto / 100)
  preco_final = preco_original - valor_desconto
  return round(preco_final, 2)

while True:
  try:
    preco_original = float(input("\nDigite o preço original do produto: R$ "))
    porcentagem_desconto = float(input("Digite a porcentagem de desconto a ser aplicada (ex: 15 para 15%): "))

    preco_com_desconto = calcular_desconto(preco_original, porcentagem_desconto)
  except ValueError:
    print("Entrada inválida. Por favor, insira valores numéricos válidos.")
  else:
    print(f"\nO preço final do produto após aplicar o desconto é: R$ {preco_com_desconto:.2f}")
    break