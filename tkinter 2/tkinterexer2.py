#FAÇA UMA APLICAÇÃO QUE PEDE PARA O USUÁRIO DIGITAR QUANTO ELE GANHA POR MÊS E QUANTAS HORAS ELE TRABALHA POR MÊS E CALCULE QUANTO ELE GANHA POR HORA
#E MOSTRE NA TELA O VALOR DE HORA TRABALHADA DA COR RESPECTIVA A TABELA ABAIXO:
# 0 - 10 = VERMELHO
# 11 - 25 = LARANJA
# 26 - 50 = AZUL
# 51 PRA CIMA = ROSA




from tkinter import * 

caixa = Tk()
caixa.title("Hora trabalhada")
caixa.geometry("300x300")


def calcular_hora():
    salario = float(salario_input.get())
    horas = int(horas_input.get())
    hora_trabalhada = salario / horas
    if hora_trabalhada >= 0 and hora_trabalhada <= 10:
        resultado.configure(text=f"Você recebe por hora: R$ {hora_trabalhada:.2f}", fg="red")
    elif hora_trabalhada >= 11 and hora_trabalhada <= 25:
        resultado.configure(text=f"Você recebe por hora: R$ {hora_trabalhada:.2f}", fg="orange")
    elif hora_trabalhada >= 26 and hora_trabalhada <= 50:
        resultado.configure(text=f"Você recebe por hora: R$ {hora_trabalhada:.2f}", fg="blue")
    else:
        resultado.configure(text=f"Você recebe por hora: R$ {hora_trabalhada:.2f}", fg="pink")





salario_label = Label(text="Digite o seu salário").pack()
salario_input = Entry()
salario_input.pack()


horas_label = Label(text="Digite a quantidade de horas trabalhadas").pack()
horas_input = Entry()
horas_input.pack()


botao = Button(caixa, text="Calcular hora trabalhada", command=calcular_hora)
botao.pack()


resultado = Label(text="")
resultado.pack()





caixa.mainloop()


