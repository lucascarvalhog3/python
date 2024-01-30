class Funcionario:
    def __init__(self, id:int, nome:str, cargo:str, salario:float) -> None:
        self.id = id
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

class Empresa:
    def __init__(self) -> None:
        self.lista_funcionarios = []
        self.contador = 0

    def adicionar(self):
        nome_do_funcionario = str(input("Digite o nome do funcionário: "))
        cargo_do_funcionario = str(input("Digite o cargo do funcionário: "))
        salario_do_funcionario = float(input("Digite o salário do funcionário: "))

        funcionario = Funcionario(id=self.contador, nome=nome_do_funcionario, cargo=cargo_do_funcionario, salario=salario_do_funcionario)
        self.lista_funcionarios.append(funcionario)

        self.contador += 1

    def exluir(self):
        for funcionario in self.lista_funcionarios:
            print(f"{funcionario.id} - {funcionario.nome} | {funcionario.cargo}")

        escolha_excluir = int(input("Digite o número do funcionário que você quer excluir: "))
        if escolha_excluir >= 0 and escolha_excluir < len(self.lista_funcionarios):
            for funcionario in self.lista_funcionarios:
                if funcionario.id == escolha_excluir:
                    self.lista_funcionarios.remove(funcionario)

    def listar_funciononarios(self):
        for funcionario in self.lista_funcionarios:
            print(f"""
            ID: {funcionario.id}
            Nome: {funcionario.nome}
            Cargo: {funcionario.cargo}
            Salário: {funcionario.salario}
""")



empresa1 = Empresa()



while True:
    menu = int(input("""
    Escolha uma opção:
    1 - Adicionar funcionário
    2 - Excluir funcionário
    3 - Ver todos os  funcionários
    0 - Sair
"""))

    match menu:
        case 1:
            empresa1.adicionar()
        case 2:
            empresa1.exluir()
        case 3:
            empresa1.listar_funciononarios()
        case 0:
            break
        case _:
            print("Opção Inválida")
      
           