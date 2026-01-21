"""

4 - Crie um programa que realize consultas a cotações de moedas em relação ao Real (BRL) usando a API AwesomeAPI, mostre valor atual, máxima, mínima e data/hora da última atualização, caso a moeda não existir ou houver erro na requisição, retorne uma mensagem de erro.

"""

import requests

def consultar_cotacao(moeda):
  url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
  try:
    resposta = requests.get(url)
    resposta.raise_for_status()
    dados = resposta.json()
    chave = f"{moeda}BRL"
    if chave in dados:
      cotacao = dados[chave]
      valor_atual = cotacao["bid"]
      valor_maximo = cotacao["high"]
      valor_minimo = cotacao["low"]
      data_hora_atualizacao = cotacao["create_date"]
      return valor_atual, valor_maximo, valor_minimo, data_hora_atualizacao
    else:
      return None
  except requests.RequestException:
    return None
    
while True:
  moeda_digitada = input("\nDigite o código da moeda (ex: USD, EUR, GBP) ou 'sair' para encerrar: ").upper()
  if moeda_digitada == "SAIR":
    print("Encerrando programa...")
    break
  resultado = consultar_cotacao(moeda_digitada)
  if resultado:
    valor_atual, valor_maximo, valor_minimo, data_hora_atualizacao = resultado
    print(f"\nCotação da moeda {moeda_digitada} em relação ao BRL:")
    print(f"Valor Atual: R$ {valor_atual}")
    print(f"Valor Máximo: R$ {valor_maximo}")
    print(f"Valor Mínimo: R$ {valor_minimo}")
    print(f"Data/Hora da Última Atualização: {data_hora_atualizacao}")
  else:
    print("\nMoeda inválida ou não encontrada. Tente novamente.")