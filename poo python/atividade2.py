# QUESTÃO 2:
class Pessoa:
    def __init__(self, nome:str, idade:int, peso:float, genero):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.genero = genero


pessoa = Pessoa(nome="João", idade=35, peso=98, genero="Masculino")

print(f"Eu me chamo {pessoa.nome}, tenho {pessoa.idade} anos, {pessoa.peso}Kg e me indetifico com o gênero {pessoa.genero}")
