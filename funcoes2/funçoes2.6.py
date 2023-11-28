# Implemente uma função lambda que receba um número e verifique se ele é divisível
# por 3 e por 5. A função deve retornar "divisível" se a condição for satisfeita e "não
# divisível" caso contrário.

divisivel_3_5 = lambda numero : "divisível" if numero % 3 == 0 and numero % 5 == 0 else "não é divisível"

numero = int(input("Digite um número: "))
print(divisivel_3_5(numero))