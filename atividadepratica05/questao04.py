"""

4 - Crie um programa que calcule a quantos dias um individuo está vivo de acordo com a data do dia.

"""

from datetime import datetime

def calcular_dias_vivo(data_nascimento, data_atual):
  dias_vivo = (data_atual - data_nascimento).days
  return dias_vivo

while True:
  try:
    data_nascimento_str = input("\nDigite a data de nascimento (dd/mm/aaaa): ")
    data_nascimento = datetime.strptime(data_nascimento_str, "%d/%m/%Y").date()
    
    data_atual = datetime.now().date()

    dias_vivo = calcular_dias_vivo(data_nascimento, data_atual)
  except ValueError:
    print("Entrada inválida. Por favor, use o formato dd/mm/aaaa.")
  else:
    print(f"\nVocê está vivo há {dias_vivo} dias.")
    break
