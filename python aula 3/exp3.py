# Dado o dicionário Carro com a seguinte estrutura: {"Marca": "Ford", "Modelo": "Ka", "Ano": 2020, "Cor": "Cinza"},
# faça um programa que cheque se existe uma chave chamada "Cor" no dicionário, se existir, mude ela para "preto" se não existir delete a chave "Ano"

carro = {
"Marca": "Ford",
"Modelo": "Ka", 
"Ano": 2020,
"Cor": "Cinza"
}

if ("Cor" in carro):
    carro["Cor"] = "Preto"
else:
    del carro["Ano"]


print(carro)




