# FAÇA UMA FUNÇÃO QUE RECEBE UMA PALAVRA QUALQUER E RETORNE ESSA MESMA PALAVRA TODA EM MAIÚSCULO
# FAÇA UM PROGRAMA QUE PEDE PARA O USUÁRIO DIGITAR UMA PALAVRA QUALQUER
# E MOSTRE NA TELA ESSA PALAVRA TODA EM MAÍUSCULO USANDO A FUNÇÃO QUE VOCÊ CRIOU.

def tranforma_maiusculo(texto:str):
    return texto.upper()

palavra = str(input("digite uma palavra: "))
print(tranforma_maiusculo(texto=palavra))
