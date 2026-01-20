"""

2-  Crie uma função que verifique se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente, ignorando espaços e pontuação). Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”.

"""

def palindromo(texto):
  texto_limpo = ''.join(caractere.lower() for caractere in texto if caractere.isalnum())
  return texto_limpo == texto_limpo[::-1]

while True:
  entrada = input("\nDigite uma palavra ou frase para verificar se é um palíndromo (ou 'sair' para encerrar): ")
  if entrada.lower() == 'sair':
    break
  if palindromo(entrada):
    print("Sim, é um palíndromo.")
  else:
    print("Não, não é um palíndromo.")
