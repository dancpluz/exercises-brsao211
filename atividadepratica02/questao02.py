"""

2- Calculadora de Desconto
Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

* Nome do produto: "Camiseta"
* Preço original: R$ 50.00
* Porcentagem de desconto: 20%
O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.

"""

nome_produto = input("Digite o nome do produto: ")
preco_original = float(input("Digite o preço unitário do produto (R$): "))
porcentagem_desconto = float(input("Digite a porcentagem de desconto (%): "))

valor_desconto = (porcentagem_desconto / 100) * preco_original
preco_final = preco_original - valor_desconto

print(f"\nProduto: {nome_produto}")
print(f"Preço original: R$ {preco_original:.2f}")
print(f"Porcentagem de desconto: {porcentagem_desconto}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")