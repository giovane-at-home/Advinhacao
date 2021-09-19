print("*******************************")
print("Bem vindo ao jogo de advinhação")
print("*******************************")

import random

numero_secreto = random.randrange(1,101)
tentativas_max = 0
pontos = 1000

print("Escolha o nível desejado:")
print("(1)Fácil (2)Médio (3)Difícil")

nivel = int(input("Digite o nível desejado: (Apenas valor)"))

if(nivel==1):
  tentativas_max = 10
elif(nivel==2):
  tentativas_max = 6
elif(nivel==3):
  tentativas_max = 3

for tentativa_atual in range(1, tentativas_max + 1):
  print("Tentativa {} de {}".format(tentativa_atual, tentativas_max))
  
  numeroUser = input("Digite um número entre 0 e 100: ")
  print("Você digitou {}".format(numeroUser))
  numeroInt = int(numeroUser)
  
  if(numeroInt < 1 or numeroInt > 100):
    print("O número escolhido foi {}, o mesmo é menor que 1 ou maior que 100".format(numeroInt))
    continue
 
  acertou = numeroInt == numero_secreto
  menor = numeroInt < numero_secreto
  maior = numeroInt > numero_secreto
 
  if(acertou):
    print("Você acertou e fez {} pontos!" .format(pontos))
    break

  else:
    if(menor):
      print("Seu chute foi menor que o número escolhido")
    elif(maior):
      print("Seu chute foi maior que o número escolhido")
    pontos_perdidos = abs(numero_secreto - numeroInt)
    pontos = pontos - pontos_perdidos

print("Fim do jogo! O número escolhido foi {}".format(numero_secreto))