from tkinter import *

class mudaCor:
    def __init__(self, toplevel):

        self.frame = Frame(toplevel)
        self.frame.pack()

        self.texto = Label(self.frame, text = 'Clique para ficar amarelo')
        self.texto['width'] = 26
        self.texto['height'] = 3
        self.texto.pack()

        self.botaoVerde = Button(self.frame, text = 'Clique')
        self.botaoVerde['background'] = 'green'
        self.botaoVerde.bind("<Button-1>", self.mudarCor)
        self.botaoVerde.pack()

    def mudarCor(self, event):
        if self.botaoVerde['bg'] == 'green':
            self.botaoVerde['bg'] = 'yellow'
            self.texto['text'] = 'Clique para ficar verde'
        else:
            self.botaoVerde['bg'] = 'green'
            self.texto['text'] = 'Clique para ficar amarelo'

raiz = Tk()
mudaCor(raiz)
raiz.mainloop()
