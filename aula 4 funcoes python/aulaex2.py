# faça uma função que pede peso e altura, e calcule IMC 
# form: IMC = PESO / ALTURA** 2

# FAÇA UM PROGRAMA QUE PEDE PESO E ALTURA DE 4 USUARIOS, CALCULE O IMC DE CADA UM USANDO A FUNÇÃO CRIADA E ADICIONE EM UMA LISTA ESSE IMC

# NO FINAL DO PRGRAMA VOCE DEVE TER UMA LISTA COM 4 IMC`S DENTRO 

# MOSTRE NA TELA OS 4 IMC`S

# imc = peso/ altura** 2

def calcular_imc(p,a):
  return p / a **2

lista_de_imcs = []

for i in range(1,5):
  peso = float(input(f"Digite o {i}º peso: "))
  altura = float(input(f"Digite a {i}ª altura: "))
  imc = calcular_imc(peso, altura)
  lista_de_imcs.append(imc)

for imc in lista_de_imcs:
  print(f"IMC: {imc:.2f}")

# faça uma função que pede peso e altura, e calcule IMC 
# form: IMC = PESO / ALTURA** 2

# FAÇA UM PROGRAMA QUE PEDE PESO E ALTURA DE 4 USUARIOS, CALCULE O IMC DE CADA UM USANDO A FUNÇÃO CRIADA E ADICIONE EM UMA LISTA ESSE IMC

# NO FINAL DO PRGRAMA VOCE DEVE TER UMA LISTA COM 4 IMC`S DENTRO 

# MOSTRE NA TELA OS 4 IMC`S

# imc = peso/ altura** 2

def calcular_imc(p,a):
  return p / a **2

lista_de_usuarios = []

for i in range(1,5):
  nome = str(input(f"Digite o {i} nome: "))
  peso = float(input(f"Digite o {i}º peso: "))
  altura = float(input(f"Digite a {i}ª altura: "))
  imc = calcular_imc(peso, altura)
  lista_de_usuarios.append({
    "name": nome,
    "weight": peso,
    "height": altura,
    "imc": imc
    })

for item in lista_de_usuarios:
  print(f"""
      Nome: {item["name"]}
      Altura: {item["height"]}
      Peso: {item["weight"]}
      IMC: {item["imc"]:.2f}
""")
