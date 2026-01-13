"""

3- Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.

"""

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32
def celsius_to_kelvin(c):
    return c + 273.15
def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9
def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15
def kelvin_to_celsius(k):
    return k - 273.15
def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

temp = float(input("Digite a temperatura: "))
origem = input("Digite a unidade de origem (C, F, K): ").upper()
destino = input("Digite a unidade de destino (C, F, K): ").upper()

if origem == destino:
    resultado = temp
elif origem == "C" and destino == "F":
    resultado = celsius_to_fahrenheit(temp)
elif origem == "C" and destino == "K":
    resultado = celsius_to_kelvin(temp)
elif origem == "F" and destino == "C":
    resultado = fahrenheit_to_celsius(temp)
elif origem == "F" and destino == "K":
    resultado = fahrenheit_to_kelvin(temp)
elif origem == "K" and destino == "C":
    resultado = kelvin_to_celsius(temp)
elif origem == "K" and destino == "F":
    resultado = kelvin_to_fahrenheit(temp)
else:
    print("Unidade inválida.")
    exit()

print(f"\n{temp}°{origem} é igual a {resultado:.2f}°{destino}")
