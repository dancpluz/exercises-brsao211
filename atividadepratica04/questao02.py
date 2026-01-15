"""

2 - Criar um código que registre as notas de alunos e calcular a média da turma.

"""

notasTotal = 0
quantidadeAlunos = 0

while True:
  try:
    entradaNota = input("\nDigite a nota do aluno (ou 'media' para ver a média da turma): ")
    if entradaNota.lower() == 'media':
      if quantidadeAlunos > 0:
        mediaNotas = notasTotal / quantidadeAlunos
        print(f"\nA média da turma é: {mediaNotas:.2f}")
      else:
        print("\nNenhuma nota válida foi inserida.")
      continue
    if entradaNota.lower() == 'sair':
      break
    
    nota = float(entradaNota)
    if 0 <= nota <= 10:
      notasTotal += nota
      quantidadeAlunos += 1
    else:
      print("Por favor, insira uma nota válida entre 0 e 10.")
  except ValueError:
    print("Entrada inválida. Por favor, insira um número ou 'sair'.")

if quantidadeAlunos > 0:
  mediaNotas = notasTotal / quantidadeAlunos
  print(f"\nA média da turma ({quantidadeAlunos} alunos) é: {mediaNotas:.2f}")
else:
  print("\nNenhuma nota válida foi inserida.")