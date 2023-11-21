#faça uma função que recebe 3 numeros e retorna qual o maior dos 3

# faça um programa que pede para o usuario digitar 3 números, e mostre qual o maior dos 3 usando a função que voce criou


def maior(n1,n2,n3):
  if n1 >= n2 and n1 >= n3:
    return n1
  elif n2 >= n1 and n2 >= n3:
    return n2
  elif n3 >= n1 and n3 >= n2:
    return n3

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

print(maior(numero1, numero2, numero3))

# faça uma função que recebe 3 numeros e retorna qual o maior dos 3

# faça um programa que pede para o usuario digitar 3 números, e mostre qual o maior dos 3 usando a função que voce criou

def maior(n1,n2,n3):
  if n1 >= n2 and n1 >= n3:
    return n1
  elif n2 >= n1 and n2 >= n3:
    return n2
  elif n3 >= n1 and n3 >= n2:
    return n3
  
lista_de_numeros = []
for i in range(1,4):
  numero = int(input(f"Digite o {i}º número: "))
  lista_de_numeros.append(numero)

print(maior(lista_de_numeros[0], lista_de_numeros[1], lista_de_numeros[2]))

# faça uma função que recebe 3 numeros e retorna qual o maior dos 3

# faça um programa que pede para o usuario digitar 3 números, e mostre qual o maior dos 3 usando a função que voce criou

def maior(lista):
  maior_numero = 0
  for numero in lista:
    if numero > maior_numero:
      maior_numero = numero
  if maior_numero == 0:
    return "Digite números positivos"
  else:
    return maior_numero


lista_de_numeros = []
for i in range(1,4):
  numero = int(input(f"Digite o {i}º número: "))
  lista_de_numeros.append(numero)

print(maior(lista_de_numeros))




    

    
    
    
