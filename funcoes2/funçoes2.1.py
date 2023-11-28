# faça uma função lambda que recebe um numero e retorna se ele é positivo ou negativo

# faça um programa que pede para o usuario digitar um número e chame a função que você criou para mostrar 
# se o número é positivo ou negativo

positivo_negativo = lambda numero : "positivo" if numero >= 0 else "negativo"

numero = int(input("Digite um número: "))

print(positivo_negativo(numero))