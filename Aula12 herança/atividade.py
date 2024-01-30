#CRIE UMA CLASSE CHAMADO Gato QUE TEM OS ATRIBUTOS:
#nome(str), idade(int), peso(float), cor(str), raça(str)
#E OS MÉTODOS:
#miar() que retorna "O gato {nome do gato} está miando"
#comer() que retrona "O gato {nome do gato} está comendo"
#ver_informações() que retorna todos os atributos do gato
#INSTANCIE DOIS GATOS E USE OS MÉTODOS NOS DOIS

class Gato:
    def __init__(self, nome:str, idade: int, peso:float, cor:str, raca:str) -> None:
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.cor = cor
        self.raca = raca
    
    def miar(self):
        return f"O gato {self.nome} está miando"
    
    def comer(self):
        return f"O gato {self.nome} está comendo"
    
    def ver_informacoes(self):
        return f"""
        Nome do gato: {self.nome}
        Idade do gato: {self.idade} anos
        Peso do gato: {self.peso} Kg
        Cor do gato: {self.cor}
        Raça do gato: {self.raca}
"""    

nome_do_gato = str(input("Digite o nome do gato: "))
idade_do_gato = int(input("Digite a idade do gato: "))
peso_do_gato = float(input("Digite o peso do gato: "))
cor_do_gato = str(input("Digite a cor do gato: "))
raca_do_gato = str(input("Digite a raça do gato: "))


gato1 = Gato(nome=nome_do_gato, idade=idade_do_gato, peso=peso_do_gato, cor=cor_do_gato, raca=raca_do_gato)
gato2 = Gato(nome="Salem", idade=100, peso=1, cor="Preto", raca="Bruxa")

print(gato1.miar())
print(gato1.comer())
print(gato1.ver_informacoes())


print(gato2.miar())
print(gato2.comer())
print(gato2.ver_informacoes())


    