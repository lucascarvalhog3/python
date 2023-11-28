# faça uma função que recebe uma palavra e retorna a quantidade de vogais que essa palavra contém 

# faça uma programa que pede para o usuário digitar uma palavra e se essa palavra digitada tiver 
# mais de 3 vogais mostre na tela "mais de 3 vogais" se não mostre na tela "menos 3 vogais"

def contar_vogais(texto : str):
    contador = 0
    for vogais in texto:
        if vogais in "aeiou":
            contador = contador + 1
    return contador 

palavra = str(input("digite uma palavra" ))
quantidade = contar_vogais(texto = palavra)

if quantidade > 3:
    print(f"A {palavra} tem mais de 3 vogais")
elif quantidade < 3:
    print(f"A {palavra} tem menos de 3 vogais")
else:
    print(f"A {palavra} tem exatamente 3 vogais")



    
    
