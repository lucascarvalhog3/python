USANDO O DICIONÁRIO pessoa COM A SEGUINTE ESTRUTURA:
{"nome": "João", "idade": 30, "cpf": "000.000.000-00"}
FAÇA UM PROGRAMA QUE CHECA SE O USUÁRIO É MAIOR OU MENOR DE IDADE
SE ELE FOR MAIOR DE IDADE ADICIONE UM NOVO CAMPO NO DICIONÁRIO COM A CHAVE "habilitacao" E O VALOR True
SE NÃO MUDA O NOME DELE PARA "Joãozinho"


# pessoa = {
#     "nome": str(input("Digite seu nome: ")),
#     "idade": int(input("Digite sua idade: ")),
#     "cpf": str(input("Digite seu cpf: "))
# }

# if pessoa["idade"] >= 18:
#     pessoa["habilitação"] = True
# else:
#     pessoa["nome"] = "Joãozinho"

# print(pessoa)


nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
cpf = str(input("Digite seu cpf: "))

pessoa = {
    "nome": nome,
    "idade": idade,
    "cpf": cpf
}

if pessoa["idade"] >= 18:
    pessoa["habilitação"] = True
else:
    pessoa["nome"] = "Joãozinho"

print(pessoa)




