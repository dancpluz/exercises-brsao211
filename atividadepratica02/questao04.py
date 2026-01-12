"""

4- Calculadora de Consumo de Combustível
Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:

* Distância percorrida: 300 km
* Combustível gasto: 25 litros
O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais.

"""

distancia_percorrida = float(input("Digite a distância percorrida (km): "))  # em km
combustivel_gasto = float(input("Digite o combustível gasto (litros): "))  # em litros

consumo_medio = distancia_percorrida / combustivel_gasto

print(f"\nDistância percorrida: {distancia_percorrida} km")
print(f"Combustível gasto: {combustivel_gasto} L")
print(f"Consumo médio: {consumo_medio:.2f} km/l")
