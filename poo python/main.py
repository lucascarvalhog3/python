# VERSÃO 1
class Celular:
    def __init__(self, marca, modelo, cor, ano, armazenamento):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.armazenamento = armazenamento


celular1 = Celular(marca="Samsung", modelo="S22 Ultra", cor="Cinza", ano=2022, armazenamento=256)
celular2 = Celular("Apple", "Iphone 15", "Preto", 2023, 512)
celular3 = Celular(modelo="S23", armazenamento=512, marca="Samsung", cor="Branco", ano=2023)


marca_do_celular = str(input("Digite a marca do celular: "))
modelo_do_celular = str(input("Digite o modelo do celular: "))
cor_do_celular = str(input("Digite a cor do celular: "))
ano_do_celular = int(input("Digite o ano do celular: "))
armazenamento_do_celular = int(input("Digite o armazenamento do celular: "))


celular4 = Celular(marca=marca_do_celular, modelo=modelo_do_celular, cor=cor_do_celular, ano=ano_do_celular, armazenamento=armazenamento_do_celular)


print(celular1.modelo, celular1.cor)
print(celular2.modelo)
print(celular3.modelo)
print(f"O celular {celular1.modelo} tem {celular1.armazenamento}GB de armazenamento")






 # VERSÃO 2
class Celular:
    def __init__(self, marca, modelo, cor, ano, armazenamento):
        self.brand = marca
        self.model = modelo
        self.color = cor
        self.year = ano
        self.storage = armazenamento


celular1 = Celular(marca="Samsung", modelo="S22 Ultra", cor="Cinza", ano=2022, armazenamento=256)
celular2 = Celular("Apple", "Iphone 15", "Preto", 2023, 512)
celular3 = Celular(modelo="S23", armazenamento=512, marca="Samsung", cor="Branco", ano=2023)


marca_do_celular = str(input("Digite a marca do celular: "))
modelo_do_celular = str(input("Digite o modelo do celular: "))
cor_do_celular = str(input("Digite a cor do celular: "))
ano_do_celular = int(input("Digite o ano do celular: "))
armazenamento_do_celular = int(input("Digite o armazenamento do celular: "))


celular4 = Celular(marca=marca_do_celular, modelo=modelo_do_celular, cor=cor_do_celular, ano=ano_do_celular, armazenamento=armazenamento_do_celular)


print(celular1.model, celular1.color)
print(celular2.model)
print(celular3.model)
print(f"O celular {celular1.model} tem {celular1.storage}GB de armazenamento")










