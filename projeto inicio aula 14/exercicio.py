# FAÇA UMA CLASSE PAI CHAMADA Veículo QUE TENHA OS ATRIBUTOS:
# marca(str), modelo(str), cor(str), ano(int)
# E UM ATRIBUTO INTERNO CHAMADO velocidade_atual QUE COMEÇA COM 0
# self.velocidade_atual = 0
# E OS MÉTODOS:
# acelerar(velocidade_acelerada) QUE EDITA A velocidade_atual PARA ELA MESMO + A velocidade_acelerada E RETORNA UMA MENSAGEM TIPO "O veículo {self.modelo} está acelerando"
# E O MÉTODO:
# freiar() QUE SEMPRE REDUZ EM 10 A velocidade_atual E RETORNA UMA MENSAGEM TIPO "O veículo {self.modelo}
# E O MÉTODO:
# buzinar() QUE RETORNA "Som indefinido"

# CRIE UMA CLASSE FILHA CHAMADA Carro QUE TEM O ATRIBUTO ADICIONAL:
# qtde_portas(int)
# FAÇA UM POLIMORFISMO NO MÉTODO buzinar() ALTERANDO O RETORNO DELE PARA "bi bi"

# CRIE UMA CLASSE FILHA CHAMADA Navio QUE FAZ UM POLIMORFISMO NO MÉTODO DE buzinar() ALTERANDO O RETORNO PARA "FOMMMM" 

# ENCAPSULE TODOS OS DADOS

# INSTANCIE UM CARRO E UM NAVIO

# TESTE OS MÉTODOS DE ACELERAR E FREIAR



#RESOLUÇÃO
class Veiculo:
    def __init__(self, marca:str, modelo:str, cor: str, ano: int) -> None:
        self.__marca = marca
        self.__modelo = modelo
        self.__cor = cor
        self.__ano = ano
        self.__velocidade_atual = 0

    def getMarca(self):
        return self.__marca
    
    def setMarca(self,novo_valor:str):
        self.__marca = novo_valor
        return "Valor alterado com sucesso"
    

    def getModelo(self):
        return self.__modelo
    
    def setModelo(self,novo_valor:str):
        self.__modelo = novo_valor
        return "Valor alterado com sucesso"
    


    def getCor(self):
        return self.__cor
    
    def setCor(self,novo_valor:str):
        self.__cor = novo_valor
        return "Valor alterado com sucesso"
    


    def getAno(self):
        return self.__ano
    
    def setAno(self,novo_valor:int):
        self.__ano = novo_valor
        return "Valor alterado com sucesso"
    
    def acelerar(self,velocidade_acelerada:float):
        self.__velocidade_atual += velocidade_acelerada
        return f"O veículo acelerou e está a {self.__velocidade_atual}"

    def freiar(self):
        if self.__velocidade_atual >= 10:
            self.__velocidade_atual -= 10
            return f"O veículo freio e está a {self.__velocidade_atual}"
        else:
            self.__velocidade_atual = 0
            return f"O veículo parou"
    
    def buzinar(self):
        return "Som indefinido"


class Carro(Veiculo):
    def __init__(self, marca: str, modelo: str, cor: str, ano: int, qtde_portas:int) -> None:
        super().__init__(marca, modelo, cor, ano)
        self.qtde_portas = qtde_portas
    
    def getQtdePortas(self):
        return self.__qtde_portas
    
    def setQtdePortas(self,novo_valor:int):
        self.__qtde_portas = novo_valor
        return "Valor alterado com sucesso"
    
    def buzinar(self):
        return "bi bi"
    

class Navio(Veiculo):
    def __init__(self, marca: str, modelo: str, cor: str, ano: int) -> None:
        super().__init__(marca, modelo, cor, ano)
    
    def buzinar(self):
        return "Foommmmm"
    

carro1 = Carro(marca="Fiat", modelo="Palio", cor="Cinza", ano=2008, qtde_portas=2)
navio1 = Navio(marca="Harland Wolf", modelo="Titanic", cor="Branco", ano=1909)

print(carro1.buzinar())
print(navio1.buzinar())

print(carro1.acelerar(velocidade_acelerada=50))
print(carro1.acelerar(velocidade_acelerada=20))
print(carro1.acelerar(velocidade_acelerada=15))
print(carro1.freiar())
print(carro1.freiar())
print(carro1.freiar())
print(carro1.freiar())
print(carro1.freiar())
print(carro1.freiar())
print(carro1.freiar())
print(carro1.freiar())
print(carro1.freiar())
print(navio1.acelerar(velocidade_acelerada=160))