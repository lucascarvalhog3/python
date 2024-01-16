#FAÇA UMA APLICAÇÃO PARA SIMULAR UM SEMÁFORO, A APLICAÇÃO TERÁ 3 BOTÕES DAS CORES RESPECTIVAS:
#vermelho
#amarelo
#verde
#E O semaforo PODERÁ CLICAR NO BOTÃO, AO CLICAR NO BOTÃO VERMELHO, APARECERÁ UMA MENSAGEM NA TELA ESCRITO "PARE", NO AMARELO UMA MENSAGEM "ATENÇÃO" NO VERDE UMA MENSAGEM "CONTINUE"


#VERSÃO 2
from tkinter import *

box = Tk()
box.title("Semáforo")
box.geometry("150x300")

def checar_cor(cor):
    if cor == "vermelho":
        resultado.configure(text="Pare!")
    elif cor == "amarelo":
        resultado.configure(text="Atenção!")
    elif cor == "verde":
        resultado.configure(text="Prossiga!")

bt_vermelho = Button(bg="red", width=20, height=4, command=lambda : checar_cor("vermelho"))
bt_vermelho.pack()

bt_amarelo = Button(bg="yellow", width=20, height=4, command=lambda : checar_cor("amarelo"))
bt_amarelo.pack()

bt_verde = Button(bg="green", width=20, height=4, command=lambda : checar_cor("verde"))
bt_verde.pack()

resultado = Label(text="", font=("Arial", 14))
resultado.pack()

box.mainloop()