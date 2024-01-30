#crie uma classe calculadora que tenha metodos para realizar matematicas basicas ( +, -, *, /)

class Calculadora:
    def __init__(self):
        self.resultado = 0
    
    def somar(self,n1:float, n2:float):
        self.resultado = n1 + n2
        return self.resultado

    def subtrair(self,n1:float, n2:float):
        self.resultado = n1 - n2
        return self.resultado
    
    def multiplicar(self,n1:float, n2:float):
        self.resultado = n1 * n2
        return self.resultado
    
    def dividir(self,n1:float, n2:float):
        if n2 != 0:
            self.resultado = n1 / n2
            return self.resultado
        else:
            return "Error, não é possível dividir por 0"
        
    


calculadora1 = Calculadora()

while True:
    menu = int(input("""
        Escolha uma opção:
        1 - Somar
        2 - Subtrair
        3 - Multiplicar
        4 - Dividir
        0 - Sair
    """))

    numero1 = float(input("Digite o primeiro valor: "))
    numero2 = float(input("Digite o segundo valor: "))

    match menu:
        case 1:
            print(calculadora1.somar(n1=numero1, n2=numero2))
        case 2:
            print(calculadora1.subtrair(n1=numero1, n2=numero2))
        case 3:
            print(calculadora1.multiplicar(n1=numero1, n2=numero2))
        case 4:
            print(calculadora1.dividir(n1=numero1, n2=numero2))
        case 0:
            break
        case _:
            print("Opção Inválida")