"""

3 - Criar um código que serve para verificar se uma senha digitada pelo usuário atende a critérios básicos de segurança.
a - deve ter pelo menos 8 caracteres.
b - deve conter pelo menos um número.

"""

while True:
  try:
    senha = input("\nDigite a senha que deseja verificar (ou 'sair' para encerrar): ")
    
    if senha.lower() == 'sair':
      break

    if len(senha) < 8:
      raise ValueError("Senha fraca: A senha deve ter pelo menos 8 caracteres.")

    if not any(caractere.isdigit() for caractere in senha):
      raise ValueError("Senha fraca: A senha deve conter pelo menos um número.")

    print("Senha forte: A senha atende aos critérios de segurança.")
    
  except ValueError as erro:
    print(erro)