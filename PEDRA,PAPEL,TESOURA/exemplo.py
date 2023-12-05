# from random import choice

# lista_de_opcoes = ["Azul", "Vermelho", "Amarelo", "Verde"]
# escolha = choice(lista_de_opcoes)

# while True:
#     decisao = str(input("Digite sua decisão: "))
#     if decisao == "sair":
#         break
#     elif decisao in lista_de_opcoes:
#         print("vamos jogar")
    
# print(escolha)


contador1 = 0
contador2 = 0


while True:
    escolha_1 = int(input("Digite um número: "))
    
    if escolha_1 == 999:
        break

    escolha_2 = int(input("Digite outro número: "))


    if escolha_1 > escolha_2:
        contador1 +=1
    else:
        contador2 +=1

if contador1 > contador2:
    print(f"O jogador um venceu de {contador1} a {contador2}")
elif contador2 > contador1:
    print(f"O jogador dois venceu de {contador2} a {contador1}")
else:
    print("Empate")
