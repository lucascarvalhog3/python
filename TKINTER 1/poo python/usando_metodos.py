# USANDO MÉTODOS

class Celular:
    def __init__(self, marca:str, modelo:str, cor:str, ano:int, armazenamento:int):
        self.brand = marca
        self.model = modelo
        self.color = cor
        self.year = ano
        self.storage = armazenamento

    def ligacao(self, numero):
        return f"O celular {self.model} está fazendo uma ligação para o número:{numero} "

    def desligar(self):
        return f"O celular {self.model} está desligando."
    
    def ver_informacoes(self):
        return f"""
        Marca: {self.brand}
        Modelo: {self.model}
        Cor: {self.color}
        Ano de Fabricação: {self.year}
        Armazenamento interno: {self.storage}
    """


celular1 = Celular(marca="Samsung", modelo="S23 Plus", cor="Prata", ano=2023, armazenamento=512)

print(celular1.desligar())

numero_de_celular = str(input("Digite o número do celular: "))
print(celular1.ligacao(numero=numero_de_celular))
print(celular1.ligacao(numero="(82) 98521-1464"))
print(celular1.ligacao(numero="(11) 98943-3647"))

print(celular1.ver_informacoes())









