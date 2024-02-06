#FAÇA UMA CLASSE PAI CHAMADO Dispositivo QUE TENHA COMO ATRIBUTO DO init:
#marca(str), modelo(str), cor(str)
#E UM ATRIBUTO INTERNO CHAMADO 
#ligado QUE É INICIADO COMO False
#ligado = False
#E DOIS MÉTODOS UM CHAMADO:
#ligar() QUE MUDA O ESTADO DO ATRIBUTO ligado PARA True E EXIBE UMA MENSAGEM TIPO "{self.modelo} ligou"
#OUTRO MÉTODO CHAMADO:
#desligar() QUE MUDA O ESTADO DO ATRIBUTO ligado PARA False E EXIBE UMA MENSAGEM TIPO "{self.modelo} desligou"

#CRIE UMA CLASSE FILHA CHAMADA Smartphone QUE TENHA COMO ATRIBUTO ADICIONAL sistema_operacional(str)
#E UM MÉTODO CHAMADO:
#fazer_chamada(numero) QUE RECEBE UM NÚMERO E RETORNA "O smartphone {self.modelo} está fazendo uma chamada para {numero}

#CRIE UMA CLASS FILHA CHAMADA Notebook QUE TEM O ATRIBUTO A MAIS CHAMADO ssd(bool) E O MÉTODO
#acessar_site(site) QUE RETORNA "O notebook {self.modelo} está acessando site {site}" 

#INSTACIE DOIS Smarphones, UM notebook E UM Tablet


class Dispositivo:
    def __init__(self,marca:str, modelo:str, cor:str) -> None:
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ligado = False
    
    def ligar(self):
        if self.marca == "Negativo":
            return "Explodiu"
        else:
            if self.ligado == False:
                self.ligado = True
                return f"{self.modelo} ligou"
            else:
                return "O aparelho já se encontra ligado."
            
    def desligar(self):
        if self.ligado:
            self.ligado = False
            return f"{self.modelo} desligou"
        else:
            return "O aparelho já está desligado"
        


class Smartphone(Dispositivo):
    def __init__(self, marca: str, modelo: str, cor: str, sistema_operacional:str) -> None:
        super().__init__(marca, modelo, cor)
        self.sistema_operacional = sistema_operacional
    
    def fazer_chamada(self,numero:str):
        if self.ligado:
            return f"O smartphone {self.modelo} está fazendo uma chamada para o número {numero}"
        else:
            return "Ligue o smartphone"

class Notebook(Dispositivo):
    def __init__(self, marca: str, modelo: str, cor: str, ssd:bool) -> None:
        super().__init__(marca, modelo, cor)
        self.ssd = ssd

    def acessar_site(self,site:str):
        if self.ligado:
            return f"O notebook {self.modelo} está acessando o site {site}"
        else:
            return "Ligue o notebook"

smart1 = Smartphone(marca="Samsung", modelo="S23", cor="Prata", sistema_operacional="Android")
smart2 = Smartphone(marca="Apple", modelo="Iphone 14", cor="Branco", sistema_operacional="IOS")

note1 = Notebook(marca="Dell", modelo="G15", cor="Preto", ssd=True)

tablet1 = Dispositivo(marca="Negativo", modelo="Do Governo", cor="Preto")
tablet2 = Dispositivo(marca="Samsung", modelo="X", cor="Preto")


print(smart1.ligar())
print(smart1.fazer_chamada("8599999999"))
print(smart1.desligar())
print(smart1.fazer_chamada("8599999999"))


print(smart2.ligar())
print(smart2.fazer_chamada("8599999999"))
print(smart2.desligar())
print(smart2.fazer_chamada("8599999999"))

print(note1.ligar())
print(note1.acessar_site("www.google.com"))
print(note1.desligar())


print(tablet1.ligar())
print(tablet2.ligar())









    
    