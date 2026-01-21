"""

2 - Crie um programa que acesse a API Random User Generator para buscar um usuário fictício aleatório. exibindo o nome, e-mail e país desse usuário, caso houver erro na conexão, mostre uma mensagem de falha.


"""

import requests

def buscar_usuario_aleatorio():
  url = "https://randomuser.me/api/"
  try:
    resposta = requests.get(url)
    resposta.raise_for_status()
    dados = resposta.json()
    usuario = dados['results'][0]
    nome = f"{usuario['name']['first']} {usuario['name']['last']}"
    email = usuario['email']
    pais = usuario['location']['country']
    return nome, email, pais
  except requests.RequestException:
    return None
    
usuario = buscar_usuario_aleatorio()

if usuario:
    nome, email, pais = usuario
    print(f"Nome: {nome}\nEmail: {email}\nPaís: {pais}")
else:
    print("Falha ao buscar usuário.")