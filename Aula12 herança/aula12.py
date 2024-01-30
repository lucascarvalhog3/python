#HERANÇA
class Veiculo:
    def __init__(self, marca:str, modelo:str, ano:int, cor:str) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
    
    def ligar(self):
        return f"O veículo {self.modelo} está ligando"
    
    def desligar(self):
        return f"O veículo {self.modelo} está desligando"
    
class Carro(Veiculo):
    def __init__(self, marca: str, modelo: str, ano: int, cor: str, qtde_portas:int) -> None:
        super().__init__(marca, modelo, ano, cor)
        self.qtde_portas = qtde_portas

    def ligar_o_ar(self):
        return f"O carro {self.modelo} ligou o ar condicionado"

class Moto(Veiculo):
    def __init__(self, marca: str, modelo: str, ano: int, cor: str, cilindradas:int) -> None:
        super().__init__(marca, modelo, ano, cor)
        self.cilindradas = cilindradas

    def botar_o_descanso(self):
        return f"A moto {self.modelo} está apoiada no descanso"


carro1 = Carro(marca="Fiat", modelo="Uno", ano=2002, cor="Prata", qtde_portas=2)
moto1 = Moto(marca="BMW", modelo="G310", ano=2023, cor="Branco", cilindradas=300)




        
