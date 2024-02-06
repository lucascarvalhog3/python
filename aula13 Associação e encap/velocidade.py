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

class Veiculo:
    def __init__(self, marca: str, modelo: str, cor:str, ano: int) -> None:
        self.__marca = marca
        self.__modelo = modelo
        self.__cor = cor
        self.__ano = ano

        self.__ velocidade_atual = 0

    def acelerar(self):
        







    
