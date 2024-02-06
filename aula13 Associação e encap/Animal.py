#POLIMORFISMO
class Animal:
    def __init__(self, raca:str, cor:str, peso:float) -> None:
        self.raca = raca
        self.cor = cor
        self.peso = peso
    
    def emitir_som(self):
        return "Som indefinido"
    

class Cachorro(Animal):
    def __init__(self, raca: str, cor: str, peso: float) -> None:
        super().__init__(raca, cor, peso)
    
    def pegar_bolinha(self):
        return "O cachorro pegou a bolinha"
    
    def emitir_som(self):
        return "Au aaau"


class Gato(Animal):
    def __init__(self, raca: str, cor: str, peso: float, cor_do_olho:str) -> None:
        super().__init__(raca, cor, peso)
        self.cor_do_olho = cor_do_olho

    def amassar_paozinho(self):
        return "O gato ta amassando paozinho"
    
    def emitir_som(self):
        return "Miauuuu"

cachorrim = Cachorro(raca="Pitbull", cor="Bege", peso=8.3)
gatim = Gato(raca="Angorá", cor="branco", peso=3.5, cor_do_olho="Azul")

print(cachorrim.emitir_som())
print(gatim.emitir_som())
print(gatim.emitir_som())