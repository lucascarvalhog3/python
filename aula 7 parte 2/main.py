#calculadora
from calculadora import *

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

while True:
    menu = int(input("""
    Escolha uma operação
    1 - Somar
    2 - Subtrair
    3 - Multiplicar
    4 - Dividir
    0 - Sair
"""))
    match menu:
        case 1:
            print(somar(n1=numero1, n2=numero2))
        case 2:
            print(subtrair(n1=numero1, n2=numero2))
        case 3:
            print(multiplicar(n1=numero1, n2=numero2))
        case 4:
            print(dividir(n1=numero1, n2=numero2))
        case 0:
            break
        case _:
            print("Opção Inválida")




