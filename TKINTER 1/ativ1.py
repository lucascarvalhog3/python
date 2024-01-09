from tkinter import *

janelinha = Tk()
janelinha.title("Soma das notas")
janelinha.geometry("200x300")



def fazer_soma():
    nota1 = float(n1_input.get())
    nota2 = float(n2_input.get())
    soma = nota1 + nota2
    resultado.configure(text=f"A soma das notas foi: {soma}")



n1_label = Label(text="Digite a primeira nota", background ="red" , foreground ="white", font = ("arial", 16, "bold", "italic")).pack()

n1_input = Entry()
n1_input.pack()



n2_label = Label(text="Digite a segunda nota").pack()

n2_input = Entry()
n2_input.pack()



botao_calcular = Button(janelinha, text="Calcular soma", command=fazer_soma)
botao_calcular.pack()

resultado = Label(text="")
resultado.pack()


janelinha.mainloop()
