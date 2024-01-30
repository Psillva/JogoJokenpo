#JOGO JOKENPÔ

#Função Jogando - é aqui onde o jogo funcionará
def jogandoJokepol():
#Solicitando que os jogadres escolham sua Opção
    decisaoPrimeiroJogador = int(input(f"{primeiroPlay}, escolha uma opção:\n1 - Papel\n2 - Pedra\n3 - Tesoura\n"))
    print("\n")
    decisaoSegundoJogador = int(input(f"{segundoPlay}, escolha uma opção:\n1 - Papel\n2 - Pedra\n3 - Tesoura\n"))
    print("\n")
    
#Condição de empate, vitória e derrota    
    if decisaoPrimeiroJogador == decisaoSegundoJogador:
      return "Empate entre os jogadores!"
    elif (
      (decisaoPrimeiroJogador == 1 and decisaoSegundoJogador == 2) or
      (decisaoPrimeiroJogador == 2 and decisaoSegundoJogador == 3) or
      (decisaoPrimeiroJogador == 3 and decisaoSegundoJogador == 1)
):
      return f"O joador {primeiroPlay} venceu!"
    else:
      return f"O jogador {segundoPlay} venceu!"

print("---- MENU ----\n")

#Solicitando o nome dos dois jogadores
print("-------------------------------")
primeiroPlay = input("Digite seu nome: ")
print("-------------------------------")
segundoPlay = input("Digite seu nome: ")
print("-------------------------------")

print("\n---- Jogo Jokenpô ----\n")
resultado = jogandoJokepol() #Chamando a função "jogandoJokenol" na variável resultado
print(resultado)
jogarDeNovo = int(input("Que jogar de novo\n1 - SIM\n2 - NÃO\n"))
print("\n")

#Condição de Jogar de Novo
while jogarDeNovo == 1:
    resultado = jogandoJokepol()#Chamando a função "jogandoJokenol" na variável resultado
    print(resultado)
    jogarDeNovo = int(input("Que jogar de novo\n1 - SIM\n2 - NÃO\n"))
    print("\n")
else:
    print("Até mais tarde jogadores")
    exit()



     