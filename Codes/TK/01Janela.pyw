from tkinter import *

class Janela:
    def __init__(self, toplevel):
        self.fr1 = Frame(toplevel)
        self.fr1.pack()
        self.botao = Button(self.fr1, text = 'oi!',background = 'green', height = 3, widt = 5, fg = 'purple')
        self.botao.pack()

raiz = Tk()
Janela(raiz)
raiz.mainloop()
    
