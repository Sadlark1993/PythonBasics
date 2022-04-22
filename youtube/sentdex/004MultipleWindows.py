from tkinter import *

LARGE_FONT = ('verdana', 12)

class SeaofBTCapp(Tk):  #essa classe "seaofBTCapp" está herdando da classe Tk.
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        container = Frame(self)

        container.pack(side = "top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}                            #dicionário de frames
        
        for F in (StartPage, PageOne, PageTwo):
            frame = F(container, self)          
            self.frames[F] = frame              #conteiner adicionado ao dicionário sob o índice: StartPage
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame(StartPage)                  #O método irá mostrar o frame que está sob o índice StartPage

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

def qf(param):
    print(param)


class StartPage(Frame):
    def __init__(self, parent, controller):  #Ele disse que "parent" é a classe pai, no caso "SeaofBTCapp"
        Frame.__init__(self, parent)
        label = Label(self, text= 'Start Page', font = LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = Button(self, text = "To Page One",
                         command= lambda: controller.show_frame(PageOne))
        button1.pack()

        button2 = Button(self, text = "To Page Two",
                         command= lambda: controller.show_frame(PageTwo))
        button2.pack()

class PageOne(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text='Page One', font = LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = Button(self, text = 'To Start Page',
                         command = lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = Button(self, text = "To Page Two",
                         command= lambda: controller.show_frame(PageTwo))
        button2.pack()

class PageTwo(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text='Page Two', font = LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1= Button(self, text='To Start Page',
                        command = lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = Button(self, text = "To Page One",
                         command= lambda: controller.show_frame(PageOne))
        button2.pack()

app = SeaofBTCapp()
app.mainloop()















