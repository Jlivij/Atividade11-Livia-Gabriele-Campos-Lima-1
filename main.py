notas = {}

r = input("Digite sim para começar: ")
while r == 'sim':
  menu = int(input("\n1.Adicionar Aluno\n2.Excluir notas\n3.Exibir notas \n4.Alterar notas\n")) 
  if menu == 1:
    nome = str(input("Insira o nome do aluno: "))
    if notas.get(nome):
      print("Aluno existente")
    else:
      nota = float(input("Nota do aluno: "))
      notas[nome]=nota
    print(notas)
    
  if menu == 2:
    nome = input("Nome do aluno:")
    if nome in notas.keys():
      notas.pop(f"{nome}",nota)
      print(notas)
    else:
      print("O aluno não está cadastrado")
      print(notas)
  if menu == 3:
    print("Notas: {notas}")
    print(notas)
  elif menu == 4:
    nome=input("Nome do aluno: ")
    print(notas)
    if nome in notas.keys():
      nota=float(input("Nota do aluno", (nome)))
      print(notas)
    else:
      print("O aluno não está cadastrado")
      print(notas)
      break







notas = {}

r = input("Digite sim para começar: ")
while r == 'sim':
  menu = int(input("\n1.Adicionar Aluno\n2.Excluir notas\n3.Exibir notas \n4.Alterar notas\n")) 
i
ifif menu == 1:…
  if menu == 2:
    nome = input("Nome do aluno:")
    if nome in notas.keys():
      notas.pop(f"{nome}",nota)
      print(notas)
    else:
      print("O aluno não está cadastrado")
      print(notas)
  if menu == 3:
    print("Notas: {notas}")
    print(notas)
  elif menu == 4:
  

(
