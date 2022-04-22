from tkinter import *
from random import *

class Cobrinha:
    def __init__(self, toplevel):
        toplevel.title('cobrinha')
        self.canvas = Canvas(toplevel, width = 500, height = 500, takefocus=1)
        self.canvas.bind('<Left>', self.esquerda)
        self.canvas.bind('<Right>', self.direita)
        self.canvas.bind('<Up>', self.cima)
        self.canvas.bind('<Down>', self.baixo)
        self.canvas.bind('<Return>', self.enter)
        self.canvas.focus_force()
        self.canvas.pack()
        self.frame = Frame(toplevel)
        self.frame.pack()
        
        self.ret = self.canvas.create_rectangle
        altura = 500
        self.ret(249, 249, 255, 255, fill='black', tag='cabeca')
        self.enter('<Return>')
        self.x1, self.y1, self.x2, self.y2 = self.canvas.coords('cabeca')
        self.x3, self.y3, self.x4, self.y4 = self.canvas.coords('alvo')
        
        fonte = ('Verdana', '10')
        self.labx1 = Label(self.frame, width=4, font=fonte, text = self.x1, padx = 8)
        self.labx1.pack(side=LEFT)
        self.laby1 = Label(self.frame, width=4, font=fonte, text = self.y1, padx=8)
        self.laby1.pack(side=LEFT)
        self.labx3 = Label(self.frame, width=4, font=fonte, text = self.x3, padx=8)
        self.labx3.pack(side=LEFT)
        self.laby3 = Label(self.frame, width=4, font=fonte, text = self.y3, padx=8)
        self.laby3.pack(side=LEFT)
        

    def esquerda(self, event):
        self.canvas.move('cabeca', -3,0)
        self.x1, self.y1, self.x2, self.y2 = self.canvas.coords('cabeca')
        self.labx1['text'] = self.x1
        if self.x1 >= self.x3-6 and self.x1<=self.x3+6 and self.y1 >= self.y3-6 and self.y1<=self.y3+6:
            self.canvas.delete('alvo')
        
    def direita(self, event):
        self.canvas.move('cabeca', 3,0)
        self.x1, self.y1, self.x2, self.y2 = self.canvas.coords('cabeca')
        self.labx1['text'] = self.x1
        if self.x1 >= self.x3-6 and self.x1<=self.x3+6 and self.y1 >= self.y3-6 and self.y1<=self.y3+6:
            self.canvas.delete('alvo')
        
    def cima(self, event):
        self.canvas.move('cabeca', 0,-3)
        self.x1, self.y1, self.x2, self.y2 = self.canvas.coords('cabeca')
        self.laby1['text'] = self.y1
        if self.x1 >= self.x3-6 and self.x1<=self.x3+6 and self.y1 >= self.y3-6 and self.y1<=self.y3+6:
            self.canvas.delete('alvo')

    def baixo(self, event):
        self.canvas.move('cabeca', 0,3)
        self.x1, self.y1, self.x2, self.y2 = self.canvas.coords('cabeca')
        self.laby1['text'] = self.y1
        if self.x1 >= self.x3-6 and self.x1<=self.x3+6 and self.y1 >= self.y3-6 and self.y1<=self.y3+6:
            self.canvas.delete('alvo')

    
    def enter(self,event):
        randx = int(494*random())
        randy = int(494*random())
        self.ret(randx, randy, randx+6, randy+6, fill='black', tag='alvo')
        self.x3, self.y3, self.x4, self.y4 = self.canvas.coords('alvo')


raiz = Tk()
Cobrinha(raiz)
raiz.mainloop()
