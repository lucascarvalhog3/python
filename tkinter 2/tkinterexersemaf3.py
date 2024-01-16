
#FAÇA UMA APLICAÇÃO PARA SIMULAR UM SEMÁFORO, A APLICAÇÃO TERÁ 3 BOTÕES DAS CORES RESPECTIVAS:
#vermelho
#amarelo
#verde
#E O semaforo PODERÁ CLICAR NO BOTÃO, AO CLICAR NO BOTÃO VERMELHO, APARECERÁ UMA MENSAGEM NA TELA ESCRITO "PARE", NO AMARELO UMA MENSAGEM "ATENÇÃO" NO VERDE UMA MENSAGEM "CONTINUE"

from tkinter import *

box = Tk()
box.title("Semáforo")
box.geometry("150x300")

def vermelho():
    resultado.configure(text="Pare!")

def amarelo():
    resultado.configure(text="Atenção!")

def verde():
    resultado.configure(text="Prossiga!")


bt_vermelho = Button(bg="red", width=20, height=4, command=vermelho)
bt_vermelho.pack()

bt_amarelo = Button(bg="yellow", width=20, height=4, command=amarelo)
bt_amarelo.pack()

bt_verde = Button(bg="green", width=20, height=4, command=verde)
bt_verde.pack()


resultado = Label(text="", font=("Arial", 14))
resultado.pack()

box.mainloop()