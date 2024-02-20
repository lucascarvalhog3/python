
id_livro = 1
numero_membro = 1

class Livro:
    def __init__(self,id:int, titulo:str, autor:str) -> None:
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True


class Membro:
    def __init__(self, numero:int, nome:str) -> None:
        self.numero = numero
        self.nome = nome
        self.historico = []


class Biblioteca:
    def __init__(self) -> None:
        self.catalogo_livros = []
        self.registro_membros = []
    
    def adicionar_membro(self):
        nome_membro = str(input("Digite o nome do membro: "))

        self.registro_membros.append(Membro(numero=numero_membro, nome=nome_membro))
        numero_membro += 1

    def adicionar_livro(self):
        titulo_livro = str(input("Digite o título do livro: "))
        autor_livro = str(input("Digite o autor do livro: "))
 
        self.catalogo_livros.append(Livro(id=id_livro, titulo=titulo_livro, autor=autor_livro))
        id_livro += 1
        return "Livro adicionado com sucesso"



    def emprestar_livro(self):
        pass

    def devolver_livro(self):
        pass

    def pesquisar_livro(self):
        pass

    
    