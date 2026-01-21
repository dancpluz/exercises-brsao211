"""

3 - Crie um programa que consulte informações de um CEP na API ViaCEP, retorne logradouro, bairro, cidade e estado do CEP digitado, caso o CEP não existir ou houver erro na requisição, mostre uma mensagem de falha.

"""

import requests

def buscar_cep(cep):
  url = f"https://viacep.com.br/ws/{cep}/json/"
  try:
    resposta = requests.get(url)
    resposta.raise_for_status()
    dados = resposta.json()
    if "erro" in dados:
      return None
    logradouro = dados.get("logradouro", "")
    bairro = dados.get("bairro", "")
    cidade = dados.get("localidade", "")
    estado = dados.get("uf", "")
    return logradouro, bairro, cidade, estado
  except requests.RequestException:
    return None

while True:
  cep_digitado = input("\nDigite o CEP (somente números): ")
  resultado = buscar_cep(cep_digitado)

  if resultado:
    logradouro, bairro, cidade, estado = resultado
    print(f"\nLogradouro: {logradouro}\nBairro: {bairro}\nCidade: {cidade}\nEstado: {estado}")
    break
  else:
    print("\nCEP inválido ou não encontrado. Tente novamente.")
