executar_novo = True

while executar_novo == True:
  print("Por favor digite seu nome: ")
  nome = input()
  print("Bom dia", nome)
  print("Voce deseja executar o programa novamente? [S/N]")
  resposta = input()
  if resposta == 'S':
    executar_novo = True
  else:
    executar_novo = False
    print("Fim")
