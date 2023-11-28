# Implemente uma função lambda que receba duas strings e retorne a concatenação
# das duas, apenas se ambas as strings tiverem mais de 5 caracteres. Caso contrário,
# a função deve retornar uma mensagem de erro.

concatenacao = lambda t1, t2 : t1+t2 if len(t1) >5 and len(t2) >5 else "error"

print(concatenacao("Abel", "Jr"))
print(concatenacao("Abelardo", "Junior"))




