from tkinter import *
from datetime import *

class Controlador:
    def __init__(self, control):

        #------------(GUI)-----------------
        control.resizable(width = False, height = False)
        control.title('Controlador de Irrigação')
        control.iconbitmap(self, default = 'IconeIFMT.ico')
        self.frame1 = Frame(control)
        self.frame1.pack()
        self.lcd = Label(self.frame1, text='', width = 16, height = 4, bg = 'black',
                             fg= 'white', font= ('Arial', '20', 'bold'), anchor = 'nw')
        self.lcd.grid(row=1, column = 1, columnspan = 6, rowspan = 4, sticky = E+W)

        self.upButton = Button(self.frame1, width = 6, text = 'UP')
        self.upButton.grid(row = 5, column = 2, sticky = N+S)
        
        self.downButton = Button(self.frame1, width = 6, text = 'DOWN')
        self.downButton.grid(row=7, column = 2, sticky = N+S)
        
        self.leftButton = Button(self.frame1, width = 6, text = 'LEFT')
        self.leftButton.grid(row = 6, column = 1, sticky = E+W)
        
        self.rightButton = Button(self.frame1, width = 6, text = 'RIGHT')
        self.rightButton.grid(row = 6, column = 3, sticky = E+W)
        
        self.centerButton = Button(self.frame1, width = 6, command = self.create_sol, text = 'ENTER')
        self.centerButton.grid(row = 6, column = 2)
        
        self.space1 = Label(self.frame1, text='', width = 4)
        self.space1.grid(row=5, column=4)
        
        self.plusButton = Button(self.frame1, width = 6, text = '+')
        self.plusButton.grid(row = 5, column = 5, sticky = N+S)
        
        self.deleteButton = Button(self.frame1, width = 6, text = 'delete', bg = 'red')
        self.deleteButton.grid(row=6, column = 5, sticky = N+S)
        
        self.minusButton = Button(self.frame1, width = 6, text = '-')
        self.minusButton.grid(row = 7, column = 5, sticky = N+S)
        
        self.solenoidesArea = Canvas(control, heigh = 40, width = 250, highlightthickness = 5, highlightbackground = 'blue')
        self.solenoidesArea.pack()
        altura = 40
        self.solenoidesArea.create_oval(19, altura-21, 31, altura-9, tag = 'bomba', fill = 'black')
        self.solenoidesArea.create_oval(69, altura-21, 81, altura-9, tag = 'sol1', fill = 'black')
        self.solenoidesArea.create_oval(119, altura-21, 131, altura-9, tag = 'sol2', fill = 'black')
        self.solenoidesArea.create_oval(169, altura-21, 181, altura-9, tag = 'sol3', fill = 'black')
        self.solenoidesArea.create_oval(219, altura-21, 231, altura-9, tag = 'sol4', fill = 'black')
        self.solenoidesArea.create_text(25, altura-27, text = 'bomba', font=('Arial', '8', 'bold'), anchor = CENTER, fill = 'black')
        self.solenoidesArea.create_text(75, altura-27, text = 'sol1', font=('Arial', '8', 'bold'), anchor = CENTER, fill = 'black')
        self.solenoidesArea.create_text(125, altura-27, text = 'sol2', font=('Arial', '8', 'bold'), anchor = CENTER, fill = 'black')
        self.solenoidesArea.create_text(175, altura-27, text = 'sol3', font=('Arial', '8', 'bold'), anchor = CENTER, fill = 'black')
        self.solenoidesArea.create_text(225, altura-27, text = 'sol4', font=('Arial', '8', 'bold'), anchor = CENTER, fill = 'black')
        
        
       

        self.numSol= 0                                       #Number of solenoids / current selected solenoid
        self.currentNumSol = 1
        self.currentRow = self.currentColumn = 0            #Current row/column selected to be updated on the ENTER BUTTON press
        
        """The row starts in zero index and selects the interval 't' to be updated.
        The column starts in zero index and selects the time (hours and minutes) that will be updated, the first part is 'turn on''s time,
        the second part is 'turn of''s time."""
        
        self.lcd['text'] = 'adicionar sol ' + str(self.numSol+1)
        self.update_output()

#-------------------------Back end------------------------
    """abaixo temos o método update_output, que ficará responsável pelo estado das saídas (vermelho ou preto), para calcular qual deve ser
        o estado, o codigo calcula quanto falta para chegar, a partir de agora, no horário de início e no horario de fim do tompo t,
        se faltar mais tempo pra chegar no horario de inicio, a saída será ligada (vermelho)"""
    def update_output(self):
        if self.numSol>0:
            self.current_time = time(datetime.now().hour, datetime.now().minute)
            for i in range(0, self.numSol, 1):
                ligaLed = 0
                led = 'sol'+str(i+1)            #define a tag do led
                
                if i == 0:                      #Aqui, ele define as coordenadas do circulo led
                    config = (69, 19, 81, 31)
                elif i == 1:
                    config = (119,19,131,31)
                elif i == 2:
                    config = (169,19,181,31)
                elif i == 3:
                    config = (219,19,231,31)
                else:
                    break
                    
                sol = self.vetsole[i]
                t1iH = sol["t1"][0].hour
                t1iM = sol["t1"][0].minute
                t1fH = sol["t1"][1].hour
                t1fM = sol["t1"][1].minute

                t2iH = sol["t2"][0].hour
                t2iM = sol["t2"][0].minute
                t2fH = sol["t2"][1].hour
                t2fM = sol["t2"][1].minute

                t3iH = sol["t3"][0].hour
                t3iM = sol["t3"][0].minute
                t3fH = sol["t3"][1].hour
                t3fM = sol["t3"][1].minute

                dif_t1_i_h = sol["t1"][0].hour - self.current_time.hour         #essa variavel dif_t1_i_h significa "diferença no tempo 1 no início em horas"
                dif_t1_i_m = sol["t1"][0].minute - self.current_time.minute
                if dif_t1_i_m < 0:
                    dif_t1_i_m += 60
                    dif_t1_i_h -=1
                if dif_t1_i_h < 0:
                    dif_t1_i_h += 24
                if dif_t1_i_h == dif_t1_i_m == 0:
                    dif_t1_i_h += 24
                

                dif_t1_f_h = sol["t1"][1].hour - self.current_time.hour         #diferença no tempo 1 no final em horas
                dif_t1_f_m = sol["t1"][1].minute - self.current_time.minute
                if dif_t1_f_m < 0:
                    dif_t1_f_m += 60
                    dif_t1_f_h -=1
                if dif_t1_f_h < 0:
                    dif_t1_f_h += 24
                if dif_t1_f_h == dif_t1_f_m == 0:
                    dif_t1_f_h += 24

                dif_t2_i_h = sol["t2"][0].hour - self.current_time.hour
                dif_t2_i_m = sol["t2"][0].minute - self.current_time.minute
                if dif_t2_i_m < 0:
                    dif_t2_i_m += 60
                    dif_t2_i_h -=1
                if dif_t2_i_h < 0:
                    dif_t2_i_h += 24
                if dif_t2_i_h == dif_t2_i_m == 0:
                    dif_t2_i_h += 24

                dif_t2_f_h = sol["t2"][1].hour - self.current_time.hour
                dif_t2_f_m = sol["t2"][1].minute - self.current_time.minute
                if dif_t2_f_m < 0:
                    dif_t2_f_m += 60
                    dif_t2_f_h -=1
                if dif_t2_f_h < 0:
                    dif_t2_f_h += 24
                if dif_t2_f_h == dif_t2_f_m == 0:
                    dif_t2_f_h += 24

                dif_t3_i_h = sol["t3"][0].hour - self.current_time.hour
                dif_t3_i_m = sol["t3"][0].minute - self.current_time.minute
                if dif_t3_i_m < 0:
                    dif_t3_i_m += 60
                    dif_t3_i_h -=1
                if dif_t3_i_h < 0:
                    dif_t3_i_h += 24
                if dif_t3_i_h == dif_t3_i_m == 0:
                    dif_t3_i_h += 24

                dif_t3_f_h = sol["t3"][1].hour - self.current_time.hour
                dif_t3_f_m = sol["t3"][1].minute - self.current_time.minute
                if dif_t3_f_m < 0:
                    dif_t3_f_m += 60
                    dif_t3_f_h -=1
                if dif_t3_f_h < 0:
                    dif_t3_f_h += 24
                if dif_t3_f_h == dif_t3_f_m == 0:
                    dif_t3_f_h += 24

                
                if dif_t1_i_h > dif_t1_f_h:                                         #define quando ligar (vermelho) ou desligar (preto) o led
                    ligaLed = 1
                if dif_t1_i_h == dif_t1_f_h:
                    if dif_t1_i_m > dif_t1_f_m:
                        ligaLed = 1

                if dif_t2_i_h > dif_t2_f_h:                                         
                    ligaLed = 1
                if dif_t2_i_h == dif_t2_f_h:
                    if dif_t2_i_m > dif_t2_f_m:
                        ligaLed = 1

                if dif_t3_i_h > dif_t3_f_h:                                         
                    ligaLed = 1
                if dif_t3_i_h == dif_t3_f_h:
                    if dif_t3_i_m > dif_t3_f_m:
                        ligaLed = 1

                if ligaLed == 1:                #ligar led
                    self.solenoidesArea.delete(led)
                    self.solenoidesArea.create_oval(config, fill='red', tag = led)
                else:
                    self.solenoidesArea.delete(led)
                    self.solenoidesArea.create_oval(config, fill='black', tag = led)
                
        raiz.after(1000, self.update_output)
            
     #----------------Event handlers--------------------------
        
    def create_sol(self):
        print('enter - create_sol')
        self.solenoide = {"t1": [time(0,0,0), time(0,0,0)],
                     "t2": [time(0,0,0), time(0,0,0)],
                     "t3": [time(0,0,0), time(0,0,0)]}

        self.show_sol()

        self.centerButton['command'] = self.save_sol
        self.upButton['command'] = self.one_row_above
        self.downButton['command'] = self.one_row_beyond
        self.leftButton['command'] = self.one_column_leftside
        self.rightButton['command'] = self.one_column_rightside
        self.plusButton['command'] = self.plus
        self.minusButton['command'] = self.minus
        

        

    def save_sol(self):                                     #Saves the solenoid's data in the vector to be analyzed
        print("saved: "+ str(self.solenoide["t1"][0]))
        aux = {"t1": [time(0,0,0), time(0,0,0)],
                "t2": [time(0,0,0), time(0,0,0)],
                "t3": [time(0,0,0), time(0,0,0)]}
        aux["t1"][0] = self.solenoide["t1"][0]
        aux["t1"][1] = self.solenoide["t1"][1]
        aux["t2"][0] = self.solenoide["t2"][0]
        aux["t2"][1] = self.solenoide["t2"][1]
        aux["t3"][0] = self.solenoide["t3"][0]
        aux["t3"][1] = self.solenoide["t3"][1]
        if self.numSol == 0:
            self.vetsole = []
            self.vetsole.append(dict(aux))                   
            self.numSol =+1
        elif self.currentNumSol > len(self.vetsole):
            self.vetsole.append(dict(aux))
            self.numSol += 1
        else:
            self.vetsole[self.currentNumSol-1] = dict(aux)
        self.rightButton['command'] = self.next_sol
        self.leftButton['command'] = self.previous_sol
        self.centerButton['command'] = self.select_sol
        self.deleteButton['command'] = self.delete_sol
        self.upButton['command'] = ''
        self.downButton['command'] = ''
        self.plusButton['command'] = ''
        self.minusButton['command'] = ''
        self.currentRow = self.currentColumn = 0
        self.show_sol()
        
                                                                    #The next four methods its used to navegate through the datas to select what data will be updated
    def one_row_above(self):
        if self.currentRow > 0:
            self.currentRow = self.currentRow-1
        print('current row: '+ str(self.currentRow))

    def one_row_beyond(self):
        if self.currentRow < 2:
            self.currentRow = self.currentRow+1
        print('current row: '+ str(self.currentRow))


    def one_column_leftside(self):
        if self.currentColumn > 0:
            self.currentColumn = self.currentColumn-1
        print('current column: '+ str(self.currentColumn))

    def one_column_rightside(self):
        if self.currentColumn < 3:
            self.currentColumn = self.currentColumn+1
        print('current column: '+ str(self.currentColumn))

    def show_sol(self):
        self.lcd['text'] = str(('solenoide '+str(self.currentNumSol)+':\n'+
                            't1:  ' + str(self.solenoide["t1"][0].hour) +
                            ':' + str(self.solenoide["t1"][0].minute)+
                            ' - ' + str(self.solenoide["t1"][1].hour)+
                            ':' + str(self.solenoide["t1"][1].minute)+ '\n' +
                            't2:  ' + str(self.solenoide["t2"][0].hour) +
                            ':' + str(self.solenoide["t2"][0].minute)+
                            ' - ' + str(self.solenoide["t2"][1].hour)+
                            ':' + str(self.solenoide["t2"][1].minute)+ '\n' +
                            't3:  ' + str(self.solenoide["t3"][0].hour) +
                            ':' + str(self.solenoide["t3"][0].minute)+
                            ' - ' + str(self.solenoide["t3"][1].hour)+
                            ':' + str(self.solenoide["t3"][1].minute)))

    def plus(self):
        print('plus')
        row = self.currentRow

        if self.currentColumn == 0:
            h = self.solenoide['t'+str(row+1)][0].hour
            m = self.solenoide['t'+str(row+1)][0].minute
            h = h+1
            if h>23:
                h = h-24
            self.solenoide['t'+str(row+1)][0] = time(h, m)

        elif self.currentColumn ==1:
            h = self.solenoide['t'+str(row+1)][0].hour
            m = self.solenoide['t'+str(row+1)][0].minute
            m = m+1
            if m>59:
                m = m-60
            self.solenoide['t'+str(row+1)][0] = time(h, m)

        elif self.currentColumn == 2:
            h = self.solenoide['t'+str(row+1)][1].hour
            m = self.solenoide['t'+str(row+1)][1].minute
            h = h+1
            if h>23:
                h = h-24
            self.solenoide['t'+str(row+1)][1] = time(h, m)

        elif self.currentColumn == 3:
            h = self.solenoide['t'+str(row+1)][1].hour
            m = self.solenoide['t'+str(row+1)][1].minute
            m = m+1
            if m>59:
                m = m-60
            self.solenoide['t'+str(row+1)][1] = time(h, m)
        
        self.show_sol()

    def minus(self):
        print('minus')

        row = self.currentRow
        if self.currentColumn==0:
            h = self.solenoide['t'+str(row+1)][0].hour
            m = self.solenoide['t'+str(row+1)][0].minute
            h -= 1
            if h<0:
                h += 24
            
            self.solenoide['t'+str(row+1)][0] = time(h, m)
        
        elif self.currentColumn==1:
            h = self.solenoide['t'+str(row+1)][0].hour
            m = self.solenoide['t'+str(row+1)][0].minute
            m -= 1
            if m<0:
                m += 60
            self.solenoide['t'+str(row+1)][0] = time(h, m)

        elif self.currentColumn==2:
            h = self.solenoide['t'+str(row+1)][1].hour
            m = self.solenoide['t'+str(row+1)][1].minute
            h-=1
            if h<0:
                h+=24
            self.solenoide['t'+str(row+1)][1] = time(h, m)

        elif self.currentColumn==3:
            h = self.solenoide['t'+str(row+1)][1].hour
            m = self.solenoide['t'+str(row+1)][1].minute
            m-=1
            if m<0:
                m+=60
            self.solenoide['t'+str(row+1)][1] = time(h, m)

        
        self.show_sol()
    
    def next_sol(self):
        print('next sol')
        if self.currentNumSol < self.numSol:
            self.solenoide = self.vetsole[self.currentNumSol]
            self.currentNumSol += 1
            self.show_sol()
            self.centerButton['command'] = self.select_sol
        elif self.currentNumSol == self.numSol:
            self.lcd['text'] = 'adicionar sol ' + str(self.numSol+1)
            self.currentNumSol += 1
            self.centerButton['command'] = self.create_sol

    def select_sol(self):
        self.centerButton['command'] = self.save_sol
        self.upButton['command'] = self.one_row_above
        self.downButton['command'] = self.one_row_beyond
        self.leftButton['command'] = self.one_column_leftside
        self.rightButton['command'] = self.one_column_rightside
        self.plusButton['command'] = self.plus
        self.minusButton['command'] = self.minus

    def previous_sol(self):
        print('previous sol')
        if self.currentNumSol > 1:
            print('entrou')
            self.currentNumSol-=1
            self.solenoide = self.vetsole[self.currentNumSol-1]
            self.show_sol()
            self.centerButton['command'] = self.select_sol

    def delete_sol(self):
        print('delete')
        if self.currentNumSol == self.numSol:
            del(self.vetsole[self.currentNumSol-1])
            self.numSol -= 1
            self.lcd['text'] = 'adicionar sol ' + str(self.numSol+1)
            self.centerButton['command'] = self.create_sol

            if self.currentNumSol == 1:                     #Apagar o led do solenoide excluído
                config = (69, 19, 81, 31)
            elif self.currentNumSol == 2:
                config = (119,19,131,31)
            elif self.currentNumSol == 3:
                config = (169,19,181,31)
            elif self.currentNumSol == 4:
                config = (219,19,231,31)
            self.solenoidesArea.delete('sol'+str(self.currentNumSol))
            self.solenoidesArea.create_oval(config, fill='black', tag = 'sol'+str(self.currentNumSol))
            
        else:
            self.solenoide = {"t1": [time(0,0,0), time(0,0,0)],
                     "t2": [time(0,0,0), time(0,0,0)],
                     "t3": [time(0,0,0), time(0,0,0)]}
            self.vetsole[self.currentNumSol-1] = self.solenoide
            self.centerButton['command'] = self.save_sol
            self.select_sol()
            self.show_sol()
        self.deleteButton['command'] = ''

raiz = Tk()
Controlador(raiz)
raiz.mainloop()






