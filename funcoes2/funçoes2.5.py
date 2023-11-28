# Escreva uma função lambda que receba um número e verifique se ele é maior que 10.
# Se for maior, a função deve retornar o próprio número; caso contrário, deve retornar o
# número dividido por 2.

dividir_2 = lambda numero : numero if numero > 10 else numero / 2

numero =int(input("Digite um número: "))
print(dividir_2(numero))