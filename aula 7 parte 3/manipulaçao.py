def inverter_string(texto):
    return texto[::-1]


def contar_palavras(texto:str):
    quantidade_palavras = 1
    for letra in texto.strip():
        if letra == " ":
            quantidade_palavras +=1
    return quantidade_palavras

def palindromo(texto:str):
    texto_sem_espaco = texto.replace(" ", "")
    texto_invetido = inverter_string(texto_sem_espaco)
    if texto_sem_espaco == texto_invetido:
        return "É palindromo"
    else:
        return "Não é um palindromo"
