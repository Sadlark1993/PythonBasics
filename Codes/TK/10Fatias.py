from tkinter import *

class Fatias:
    def __init__(self, raiz):
        self.canvas = Canvas(raiz, width=200, height=200)
        self.canvas.pack()
        self.frame=Frame(raiz)
        self.frame.pack()
        self.frame2 = Frame(raiz, pady = 10)
        self.frame2.pack()

        self.altura = 200

        self.canvas.create_oval(25, self.altura-25,
                                175, self.altura-175,
                                fill='deepskyblue', outline='darkblue')
        fonte = ('Comic Sans MS', '14', 'bold')
        Label(self.frame, text='Procentagem: ', font = fonte, fg='blue').pack(side=LEFT)
        self.porcentagem = Entry(self.frame, fg='red', font=fonte, width=5)
        self.porcentagem.focus_force()
        self.porcentagem.pack(side=LEFT)
        Label(self.frame, text='%', font = fonte, fg='blue').pack(side=LEFT)
        self.botao1=Button(self.frame, text='Desenhar', command=self.cortar, font= fonte, fg='darkblue', bg='deepskyblue')
        self.botao1.pack(side=LEFT)
        Label(self.frame2, text='Fração: ', font=fonte, fg='blue').pack(side=LEFT)
        self.dividendo = Entry(self.frame2, fg='yellow', font=fonte, width=2)
        self.dividendo.pack(side=LEFT)
        Label(self.frame2, text='/', font= fonte, fg='blue').pack(side=LEFT)
        self.divisor = Entry(self.frame2, fg='deepskyblue', font=fonte, width=2)
        self.divisor.pack(side=LEFT)
        Label(self.frame2, text='', width = 1).pack(side=LEFT)
        self.botao2=Button(self.frame2, text='Desenhar', command=self.cortarF, font=fonte, fg='darkblue', bg='deepskyblue')
        self.botao2.pack(side=LEFT)
        

    def cortar(self):
        
        self.canvas.create_oval(25, self.altura-25,
                                175, self.altura-175,
                                fill='deepskyblue', outline='darkblue')
        
        arco=self.canvas.create_arc
        fatia = float(self.porcentagem.get())*359.9/100.
        arco(25, self.altura - 25,
             175, self.altura - 175,
             fill='yellow', outline='red',
             extent = fatia)
        self.porcentagem.focus_force()

    def cortarF(self):
        
        self.canvas.create_oval(25, self.altura-25,
                                175, self.altura-175,
                                fill='deepskyblue', outline='darkblue')
        
        fatia = float(self.dividendo.get())/float(self.divisor.get())*359.9

        arco=self.canvas.create_arc
        arco(25, self.altura-25,
             175, self.altura-175,
             fill='yellow', outline='red',
             extent = fatia)
        self.dividendo.focus_force()

instancia = Tk()
Fatias(instancia)
instancia.mainloop()
        
