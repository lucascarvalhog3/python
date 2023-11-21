# crie uma função que calcule o valor/ hora do funcionario,em seguida implemente essa função em um programa de calcular hora e valor do funcionario.

def hora_trabalhada(v, hrs):
  return v / hrs

salario = float(input("Digite quanto você ganha: "))
horas = float(input("Digite quantas horas você trabalha: "))

print(f"Você ganha {hora_trabalhada(salario, horas):.2f} por hora")