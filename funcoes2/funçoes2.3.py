# Escreva uma função lambda que receba um número e verifique se ele é par ou
# ímpar. A função deve retornar "par" se o número for par e "ímpar" caso contrário.

numero_impar_par = lambda numero: "impar" if numero % 2 == 1 else "par"

print(numero_impar_par(101))