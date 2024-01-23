class Carro:
    def __init__(self, ano:int, cor:str, marca:str, modelo:str, qtde_portas:int, ar:bool, vidro:bool):
        self.ano = ano
        self.cor = cor
        self.marca = marca
        self.modelo = modelo
        self.qtde_portas = qtde_portas
        self.ar = ar
        self.vidro = vidro



carro1 = Carro(ano=2020, cor="Prata", marca="Ford", modelo="KA", qtde_portas=4, ar=True, vidro=True)

cor_do_carro = str(input("Digite a cor do carro: "))
ano_do_carro = int(input("Digite o ano do carro: "))
marca_do_carro = str(input("Digite a marca do carro: "))
modelo_do_carro = str(input("Digite o modelo do carro: "))
qtde_de_portas_do_carro = int(input("Digite a quantidade de portas do carro: "))
ar_do_carro = bool(input("O carro tem ar condicionado? "))
vidro_do_carro = bool(input("O carro tem vidro elétrico? "))

carro2 = Carro(ano=ano_do_carro, cor=cor_do_carro, marca=marca_do_carro, modelo=modelo_do_carro, qtde_portas=qtde_de_portas_do_carro, ar=ar_do_carro, vidro=vidro_do_carro)

carro3 = Carro(ano=2010, cor="Azul", marca="Fiat", modelo="Uno", qtde_portas=2, ar=False, vidro=False)


print(f"A marca do primeiro carro é: {carro1.marca} e o modelo é: {carro1.modelo}")

print(f"A marca do segundao carro é: {carro2.marca} o ano é: {carro2.ano}")

if carro2.vidro:
    print("O segundo carro tem vidro elétrico")
else:
    print("O segundo carro não tem vidro elétrico")


print(f"""
    Informações do carro 3:
    Marca: {carro3.marca}
    Modelo: {carro3.modelo}
    Ano: {carro3.ano}
    Cor: {carro3.cor}
    Quantidade de portas: {carro3.qtde_portas}
""")

if carro3.ar:
    print(f"O {carro3.marca} {carro3.modelo} tem ar condicionado")
else:
    print(f"O {carro3.marca} {carro3.modelo} não tem ar condicionado")


if carro3.vidro:
    print(f"O {carro3.marca} {carro3.modelo} tem vidro elétrico")
else:
    print(f"O {carro3.marca} {carro3.modelo} não tem vidro elétrico")






  
        
