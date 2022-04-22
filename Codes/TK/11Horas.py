from tkinter import *
from time import localtime

class Horas:
    def __init__(self, raiz):
        self.canvas = Canvas(raiz, width=250, height=100)
        self.canvas.pack()
        self.frame=Frame(raiz)
        self.frame.pack()

        self.altura=100

        #desenho do relogio--
        pol=self.canvas.create_polygon
        ret=self.canvas.create_rectangle
        self.texto=self.canvas.create_text
        self.fonte=('BankGothic Md BT', '20', 'bold')
        pol(10, self.altura-10,
            40, self.altura-90,
            220, self.altura-90,
            250, self.altura-10, fill='darkblue')
        pol(18, self.altura-15,
            45, self.altura-85,
            215, self.altura-85,
            242, self.altura-15, fill='dodgerblue')
        ret(45,self.altura-35,
            90, self.altura-65, fill='darkblue', outline='')
        ret(110, self.altura-35,
            155, self.altura-65, fill='darkblue', outline='')
        ret(175, self.altura-35,
            220, self.altura-65, fill='darkblue', outline='')
        self.texto(100, self.altura-50, tex =':', font=self.fonte, fill='yellow')
        #fim do desenho do relogio--

        self.mostrar=Button(self.frame, text='Que horas são?', command=self.mostra,
                            font=('Comic Sans MS', '11', 'bold'),
                            fg='darkblue', bg='deepskyblue')
        self.mostrar.pack(side=LEFT)

    def mostra(self):
        self.canvas.delete('digitos_HORA')
        self.canvas.delete('digitos_MIN')
        self.canvas.delete('digitos_SEG')
        HORA = str( localtime()[3] )
        MINUTO = str( localtime()[4] )
        SEGUNDO = str( localtime()[5] )
        self.texto(67.5, self.altura-50, text = HORA, fill='yellow',
                   font = self.fonte, tag='digitos_HORA')
        self.texto(132.5, self.altura-50, text=MINUTO, fill='yellow',
                   font=self.fonte, tag='digitos_MIN')
        self.texto(197.5, self.altura-50, text = SEGUNDO, fill='yellow',
                   font=self.fonte, tag='digitos_SEG')
        


instancia = Tk()
Horas(instancia)
instancia.mainloop()
