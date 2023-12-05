import random 



def escolha(usuario,maquina_escolha):
    
    if usuario == maquina_escolha:
        return "Empate"
    
    elif usuario=="PEDRA" and maquina_escolha=="TESOURA" or usuario=="PAPEL" and maquina_escolha=="PEDRA" or usuario=="tesoura" and maquina_escolha=="papel":
        return "Usuario Ganhou!!!"
    else:
        return "A Maquina Ganhou"
    

while True:
    maquina = ["pedra" , "papel", "tesoura"]

    maquina_escolha = random.choice(maquina).upper()
    print(maquina_escolha)
    usuario = str(input("""Escolha entre: 
                        PEDRA
                        PAPEL
                        TESOURA 
                                      """)).upper()

    resposta = escolha(usuario,maquina_escolha)

    if resposta == "Empate":
        print(resposta)
        break
    else:
        print(resposta)



