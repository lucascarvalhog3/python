# QUESTÃO 1:
class Cachorro:
    def __init__(self, nome:str, raca:str, idade:int):
        self.nome = nome
        self.raca = raca
        self.idade = idade

cachorrim = Cachorro(nome="Spike", raca="Vira lata", idade=4)


nome_do_cachorro = str(input("Digite o nome do cachorro: "))
raca_do_cachorro = str(input("Digite a raça do cachorro: "))
idade_do_cachorro = int(input("Digite a idade do cachorro: "))

cachorrim2 = Cachorro(nome=nome_do_cachorro, raca=raca_do_cachorro, idade=idade_do_cachorro)


print(f"Meu cachorro se chamada {cachorrim.nome}, é da raça {cachorrim.raca}, e tem {cachorrim.idade} anos de idade")

    


        
