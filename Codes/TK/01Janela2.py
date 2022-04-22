from tkinter import *

class Janela2:
    def __init__(self, toplevel):
        self.fr1 = Frame(toplevel)
        self.fr1.pack()
        self.botao = Button(self.fr1, text = 'teste', background = 'purple', height = 2, widt = 5, foreground = 'white')
        self.botao.pack()
        self.botao2 = Button(self.fr1, text = 'teste2', background = 'pink', height = 3, widt = 8, foreground = 'blue')
        self.botao2.pack()

raiz = Tk()
Janela2(raiz)
raiz.mainloop()
