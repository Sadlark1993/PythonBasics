from tkinter import *

class Calculadora:
    def __init__(self, toplevel):
        toplevel.resizable(width = False, height = False)
        toplevel.title('Calculadora')
        self.hist = Label(toplevel, text = '', width = 8, bg = 'black', fg = 'white', justify = RIGHT, font = ('Arial', '8'))
        self.hist.grid(row=0, column=1, columnspan=4, sticky = E+W)
        self.tela = Label(toplevel, text = '0', width = 8, bg = 'black', fg = 'white', justify = RIGHT, font = ('Arial', '10', 'bold'))
        self.tela.grid(row=1, column=1, columnspan=4, sticky = E+W)
        self.zero = Button(toplevel, width=4, command = self.buttonz, text = '0')
        self.zero.grid(row=2, column=1, sticky = E+W)
        self.enterB = Button(toplevel, width=4, command = self.enter, text = '=')
        self.enterB.grid(row=2, column=2, sticky = E+W)
        self.bspcB = Button(toplevel, widt = 4, command = self.backspace, text= 'C')
        self.bspcB.grid(row=2, column=3, sticky = E+W)
        self.b7 = Button(toplevel, width=4, command = self.button7, text='7')
        self.b7.grid(row=3, column=1, sticky = E+W)
        self.b8 = Button(toplevel, width = 4, command = self.button8, text = '8')
        self.b8.grid(row=3, column = 2, sticky = E+W)
        self.b9 = Button(toplevel, width = 4, command = self.button9, text = '9')
        self.b9.grid(row=3, column =3, sticky = E+W)
        self.b4 = Button(toplevel, width=4, command = self.button4, text='4')
        self.b4.grid(row=4, column=1, sticky = E+W)
        self.b5 = Button(toplevel, width=4, command = self.button5, text='5')
        self.b5.grid(row=4, column=2, sticky = E+W)
        self.b6 = Button(toplevel, width=4, command = self.button6, text='6')
        self.b6.grid(row=4, column=3, sticky = E+W)
        self.b1 = Button(toplevel, width=4, command = self.button1, text='1')
        self.b1.grid(row=5, column=1, sticky = E+W)
        self.b2 = Button(toplevel, width=4, command = self.button2, text='2')
        self.b2.grid(row=5, column=2, sticky = E+W)
        self.b3 = Button(toplevel, width=4, command = self.button3, text='3')
        self.b3.grid(row=5, column=3, sticky = E+W)
        self.plus = Button(toplevel, width=4, command=self.buttonp, text='+')
        self.plus.grid(row=2, column =4, sticky = E+W)
        self.minus = Button(toplevel, width=4, command= self.buttonm, text='-')
        self.minus.grid(row=3, column=4, sticky=E+W)
        self.mult = Button(toplevel, width=4, command=self.buttonMult, text = 'X')
        self.mult.grid(row=4, column=4, sticky=E+W)
        self.div = Button(toplevel, width=4, command=self.buttonDiv, text = ':')
        self.div.grid(row=5, column = 4, sticky=E+W)    
        self.num = 0.0
        self.operator = '+'

    def updateHist(self):
        if self.operator == '+':
            self.num = float(self.num) + float(self.tela['text'])
        elif self.operator == '-':
            self.num = float(self.num) - float(self.tela['text'])
        elif self.operator == '*':
            self.num = float(self.num) * float(self.tela['text'])
        elif self.operator == ':':
            self.num = float(self.num) / float(self.tela['text'])

    def enter(self):
        if self.operator == '+':
            self.tela['text'] = float(self.num) + float(self.tela['text'])
        elif self.operator == '-':
            self.tela['text'] = float(self.num) - float(self.tela['text'])
        elif self.operator == '*':
            self.tela['text'] = float(self.num) * float(self.tela['text'])
        elif self.operator == ':':
            self.tela['text'] = float(self.num) / float(self.tela['text'])

    def backspace(self):
        self.tela['text']='0'

    def button7(self):
        if self.tela['text'] == '0':
            self.tela['text'] = '7'
        else:
            self.tela['text'] = self.tela['text']+'7'

    def button8(self):
        if self.tela['text'] == '0':
            self.tela['text'] = '8'
        else:
            self.tela['text'] = self.tela['text']+'8'

    def button9(self):
        if self.tela['text'] == '0':
            self.tela['text'] = '9'
        else:
            self.tela['text'] = self.tela['text']+'9'
    
    def button4(self):
        if self.tela['text'] == '0':
            self.tela['text'] = '4'
        else:
            self.tela['text'] = self.tela['text']+'4'

    def button5(self):
        if self.tela['text'] == '0':
            self.tela['text'] = '5'
        else:
            self.tela['text'] = self.tela['text']+'5'

    def button6(self):
        if self.tela['text'] == '0':
            self.tela['text'] = '6'
        else:
            self.tela['text'] = self.tela['text']+'6'

    def button1(self):
        if self.tela['text'] == '0':
            self.tela['text'] = '1'
        else:
            self.tela['text'] = self.tela['text']+'1'

    def button2(self):
        if self.tela['text'] == '0':
            self.tela['text'] = '2'
        else:
            self.tela['text'] = self.tela['text']+'2'

    def button3(self):
        if self.tela['text'] == '0':
            self.tela['text'] = '3'
        else:
            self.tela['text'] = self.tela['text']+'3'

    def buttonz(self):
        if self.tela['text'] != '0':
            self.tela['text'] = self.tela['text']+'0'

    def buttonp(self):
        if self.tela['text'] == 0:
            self.num = self.tela['text']
        else:
            self.updateHist()
        
        self.tela['text'] = '0'
        self.operator = '+'
        self.hist['text'] = str(self.num) + self.operator

    def buttonm(self):
        if self.tela['text'] == 0:
            self.num = self.tela['text']
        else:
            self.updateHist()
        
        self.operator = '-'
        self.tela['text'] = '0'
        self.hist['text'] = str(self.num) + self.operator

    def buttonMult(self):
        if self.tela['text'] == 0:
            self.num = self.tela['text']
        else:
            self.updateHist()
        
        self.operator = '*'
        self.tela['text'] = '0'
        self.hist['text'] = str(self.num) + self.operator

    def buttonDiv(self):
        if self.tela['text'] == 0:
            self.num = self.tela['text']
        else:
            self.updateHist()
        
        self.operator = ':'
        self.tela['text'] = '0'
        self.hist['text'] = str(self.num) + self.operator

   


    


raiz = Tk()
Calculadora(raiz)
raiz.mainloop()

        
