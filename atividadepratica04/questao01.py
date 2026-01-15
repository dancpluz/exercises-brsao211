"""

1 - Criar um código que faça uma calculadora que tenha as operações básicas(+,-,*,/).

"""

while True:
  try:
    primeiroNumero = input("\nDigite o primeiro número: ")
    operacao = input("Digite a operação (+, -, *, /): ")
    segundoNumero = input("Digite o segundo número: ")

    primeiroNumero = float(primeiroNumero)
    segundoNumero = float(segundoNumero)

    if operacao == "+":
      resultado = primeiroNumero + segundoNumero
      print(f"O resultado de {primeiroNumero} + {segundoNumero} é: {resultado}")
    elif operacao == "-":
      resultado = primeiroNumero - segundoNumero
      print(f"O resultado de {primeiroNumero} - {segundoNumero} é: {resultado}")
    elif operacao == "*":
      resultado = primeiroNumero * segundoNumero
      print(f"O resultado de {primeiroNumero} * {segundoNumero} é: {resultado}")
    elif operacao == "/":
      resultado = primeiroNumero / segundoNumero
      print(f"O resultado de {primeiroNumero} / {segundoNumero} é: {resultado}")
    else:
      print("Operação inválida. Por favor, escolha entre +, -, * ou /.")
  except ValueError:
    print("Erro: Digite números válidos.")
  except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")