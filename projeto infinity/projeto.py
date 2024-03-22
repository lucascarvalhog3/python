import os

id_livro = 1
numero_membro = 1

class Livros:
    def __init__(self, id:int, titulo:str, autor:str):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

class Membros:
    def __init__(self, numero:int, nome:str):
        self.numero = numero
        self.nome = nome
        self.historico = []

class Biblioteca:
    def __init__(self):
        self.catalogo_livros = []
        self.registro_membros = []

    def adicionar_livro(self):
        global id_livro
        while True:
            titulo_livro = str(input("Digite o título do livro: "))
            nome_valido = all(i.isalpha() or i.isspace() or i == "-" for i in titulo_livro)
            if nome_valido:
                print("Nome válido")
                break
            else:
                print("Nome inválido, digite apenas letras")    
        while True:        
            autor_livro = str(input("Digite o autor do livro: "))
            nome_valido = all(i.isalpha() or i.isspace() or i == "." for i in autor_livro)
            if nome_valido:
                print("Nome válido")
                break
            else:
                print("Nome inválido, digite apenas letras")

        livro_criado = Livros(id=id_livro, titulo=titulo_livro, autor=autor_livro)
        
        id_livro += 1

        self.catalogo_livros.append(livro_criado)

        return f"Livro {titulo_livro} do autor {autor_livro} adicionado com sucesso!"
    

    def visualizar_catalogo(self):
        for livro in self.catalogo_livros:
            print(f""" 
                ID: {livro.id}
                Título: {livro.titulo}
                Autor: {livro.autor}
                Disponibilidade: {livro.disponivel}
""")


    def adicionar_membro(self):
        global numero_membro
        while True:
            nome_membro = str(input("Digite o nome do membro: "))
            nome_valido = all(i.isalpha() or i.isspace() for i in nome_membro)
            if nome_valido:
                print("Nome válido")
                break
            else:
                print("Nome inválido, digite apenas letras")

        membro_criado = Membros(numero=numero_membro, nome=nome_membro)
        
        numero_membro += 1

        self.registro_membros.append(membro_criado)

        return f"Membro {nome_membro} adicionado com sucesso!"


    def visualizar_membro(self):
        for membro in self.registro_membros:
            print(f""" 
                ID: {membro.numero}
                Nome: {membro.nome}


""")


    def pesquisar_livro(self):
        termo_pesquisado = str(input("""
        Pesquise por uma das opções: 
        Título do livro:
        ID do livro:
        Autor do livro: """)).lower()

        nao_tem_no_catalogo = True

        for livro_atual in self.catalogo_livros:
            if termo_pesquisado in str(livro_atual.titulo).lower() or termo_pesquisado in str(livro_atual.autor).lower() or str(livro_atual.id) == termo_pesquisado:
                nao_tem_no_catalogo = False
                print(f"""
                Informações do Livro Encontrado:
                ID do Livro: {livro_atual.id} 
                Título do Livro: {livro_atual.titulo} 
                Autor do Livro: {livro_atual.autor} 
                Status de disponibilidade do Livro: {livro_atual.disponivel} """)
        
        if nao_tem_no_catalogo:
            print("Livro não encontrado")

    
    def emprestar_livro(self):
        
        while True:
            try:
                id_membro_escolhido = int(input("Digite o ID do Membro que vai pegar o livro emprestado: "))
                break
            except:
                print("Digite apenas numeros")
        
        while True:
            try:
                id_livro_escolhido = int(input("Digite o ID do livro que o membro quer emprestado: "))
                break
            except:
                print("Digite apenas numeros")
        for membro_atual in self.registro_membros:
            if membro_atual.numero == id_membro_escolhido:        
                for livro_atual in self.catalogo_livros:
                    if livro_atual.id == id_livro_escolhido and livro_atual.disponivel == False:
                       print("O Livro não está disponivel no momento!")
                       break 
                    elif livro_atual.id == id_livro_escolhido and livro_atual.disponivel == True:
                        livro_atual.disponivel = False
                        membro_atual.historico.append(livro_atual)
                        return f"Livro {livro_atual.titulo} foi alugado para o {membro_atual.nome}"
                                            

    def devolver_livro(self):
                while True:
                    try:
                        id_livro_escolhido = int(input("Digite o ID do livro que será devolvido: "))
                        break
                    except:
                        print("Digite um NÚMEROOOOO MEU FI")
                for livro_atual in self.catalogo_livros:
                    if livro_atual.id == id_livro_escolhido and livro_atual.disponivel == False:
                        livro_atual.disponivel = True
                        return f"Livro {livro_atual.titulo} foi devolvido"



bibli1 = Biblioteca()
os.system("cls")
while True:
    menu = int(input("""
    Escolha uma opção
    1 - Adicionar Livro
    2 - Adicionar Membro
    3 - Emprestar Livro
    4 - Devolver Livro
    5 - Pesquisar Livro
    6- Print a lista de livros
    7- print a lista de membros
    0 - Sair
"""))
    match menu:
        case 1:
            print(bibli1.adicionar_livro())
        case 2:
            print(bibli1.adicionar_membro())
        case 3:
            print(bibli1.emprestar_livro())
        case 4:
            print(bibli1.devolver_livro())
        case 5:
            bibli1.pesquisar_livro()
        case 6:
            print(bibli1.visualizar_catalogo())
        
        case 7:
            print(bibli1.visualizar_membro())
        case 0:
            break
        case _:
            print("Opção Inválida")