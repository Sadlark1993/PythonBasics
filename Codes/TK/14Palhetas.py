from tkinter import *

class Palheta:
    def __init__(self,raiz):
        raiz.title('Palheta')
        self.canvas=Canvas(raiz,width=200,height=200)
        self.canvas.pack()
        self.frame = Frame()
        self.frame.pack()

        self.canvas.create_oval(15, 15, 185,185, fill='white', tag='bola')

        Label(self.frame, text='Vermelho: ').pack(side=LEFT)
        self.vermelho=Entry(self.frame, width=4)
        self.vermelho.focus_force()
        self.vermelho.pack(side=LEFT)
        Label(self.frame, text = 'Verde: ').pack(side=LEFT)
        self.verde=Entry(self.frame, width=4)
        self.verde.pack(side=LEFT)
        Label(self.frame, text='Azul: ').pack(side=LEFT)
        self.azul=Entry(self.frame, width=4)
        self.azul.pack(side=LEFT)

        Button(self.frame, text='Mostrar', command=self.misturar).pack(side=LEFT)

        self.rgb=Label(self.frame, text='', width=8, font=('Verdana', '10', 'bold'))
        self.rgb.pack()

    def misturar(self):
        cor= "#%02x%02x%02x" %(int(self.vermelho.get()), int(self.verde.get()), int(self.azul.get()))
        self.canvas.delete('bola')
        self.canvas.create_oval(15, 15, 185, 185, fill=cor, tag='bola')
        self.rgb['text']=cor
        self.vermelho.focus_force()

inst = Tk()
Palheta(inst)
inst.mainloop()
