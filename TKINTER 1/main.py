from tkinter import *

caixinha = Tk()
caixinha.title("Aula 1 TK")
caixinha.geometry("300x300")

def saudacao():
    nome = usuario_input.get()
    resultado.configure(text=f"Bem vindo {nome}")
    

usuario_label = Label(text="digite numero do usuario")
usuario_label.pack()

usuario_input = Entry()
usuario_input.pack()

botao_enviar = Button(caixinha, text="Enviar", command=saudacao)
botao_enviar.pack()

resultado = Label(text="")
resultado.pack()

caixinha.mainloop()
