# faça uma função que recebe uma cor e retorna pare! se essa cor for vermelha
# Atenção! se essa cor for amarela
# continue! se essa cor for verde
# error! se essa cor for qualquer outra

# faça um programa que pede para o usuario escolher 
# uma cor do semaforo, chame a função que voce criou e mostre na tela a mensagem respectiva cor

def cores(cor=str):

    if cor == "vermelho":
        return "pare"
    elif cor == "amarelo":
        return "atenção"
    elif cor == "verde":
        return "siga!"
    
    else:
        return "error"
cor = str(input("digite uma cor" ))
print(cores(cor))

    
