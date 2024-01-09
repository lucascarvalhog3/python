# FAÇA UMA APLICAÇÃO QUE PEDE 3 NOTAS PARA O USUÁRIO, CALCULA A MÉDIA DAS NOTAS E MOSRTA NA TELA UMA MENSAGEM CUSTOMIZADO, SENDO:
# "Você foi aprovado" COM O FUNDO VERDE E A FONTE BRANCA, SE A MÉDIA FOR MAIOR OU IGUAL A 7

# "Você foi reprovado" COM A COR DE FUNDO VERMELHO E A FONTE BRANCA, SE A MÉDIA FOR MENOR DO QUE 7

# "Aprovado com distinção" COM A FOR DE FUNDO AZUL E A FONTE BRANCA, SE A MÉDIA FOR IGUAL A 10
# CUSTOMIZE SEU PROGRAMA A VONTADE.


from tkinter import *

box = Tk()
box.title("Média das notas")
box.geometry("400x400")
box.config(bg="#0e254c")

def calcular_media():
    nota1 = float(nota1_input.get())
    nota2 = float(nota2_input.get())
    nota3 = float(nota3_input.get())
    media = (nota1 + nota2 + nota3) / 3
    if media >= 7 and media < 10:
        resultado.configure(text=f"Você foi aprovado com a média {media:.2f}", bg="#80ab83")
    elif media < 7 and media >= 0:
        resultado.configure(text=f"Você foi reprovado com a média {media:.2f}", bg="#cc141a")
    elif media == 10:
        resultado.configure(text=f"Você foi aprovado com distinção com a média {media:.2f}", bg="#5e86c8")
    else:
        resultado.configure(text=f"Média {media:.2f} é inválida", bg="#545172")



nota1_label = Label(text="Digite a primeira nota", bg="#0e254c", fg="#fff5ff").pack()
nota1_input = Entry()
nota1_input.pack()


nota2_label = Label(text="Digite a segunda nota", bg="#0e254c", fg="#fff5ff").pack()
nota2_input = Entry()
nota2_input.pack()


nota3_label = Label(text="Digite a terceira nota", bg="#0e254c", fg="#fff5ff").pack()
nota3_input = Entry()
nota3_input.pack()


botao_calcular = Button(box, text="Calcular média", command=calcular_media, bg="#d9cb81")
botao_calcular.pack()


resultado = Label(text="", bg="#0e254c", fg="#fff5ff")
resultado.pack()


box.mainloop()