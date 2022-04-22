import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
from tkinter import *
from tkinter import ttk


LARGE_FONT = ('verdana', 12)
style.use("ggplot")

f = Figure(figsize=(5,5), dpi=100)
a = f.add_subplot(111)

def animate(i):
    pullData = open("sampleData.txt", "r").read()
    dataList = pullData.split('\n')
    xList=[]
    yList=[]
    for eachLine in dataList:
        if len(eachLine)>1:
            x,y = eachLine.split(',')
            xList.append(int(x))
            yList.append(int(y))
        a.clear()
        a.plot(xList, yList)


class SeaofBTCapp(Tk):  #essa classe "seaofBTCapp" está herdando da classe Tk.
    def __init__(self, *args, **kwargs): 
        Tk.__init__(self, *args, **kwargs)
        Tk.iconbitmap(self, default="IconeIFMT.ico")
        Tk.wm_title(self, "Sea of BTC client")
        
        container = Frame(self)
        container.pack(side = "top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}                            #dicionário de frames
        
        for F in (StartPage, PageOne, PageTwo, PageThree):
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

        button1 = ttk.Button(self, text = "To Page One",
                         command= lambda: controller.show_frame(PageOne))
        button1.pack()

        button2 = ttk.Button(self, text = "To Page Two",
                         command= lambda: controller.show_frame(PageTwo))
        button2.pack()

        button3 = ttk.Button(self, text = "To Graph Page",
                         command= lambda: controller.show_frame(PageThree))
        button3.pack()


class PageOne(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text='Page One', font = LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text = 'To Start Page',
                         command = lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text = "To Page Two",
                         command= lambda: controller.show_frame(PageTwo))
        button2.pack()

class PageTwo(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text='Page Two', font = LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1= ttk.Button(self, text='To Start Page',
                        command = lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text = "To Page One",
                         command= lambda: controller.show_frame(PageOne))
        button2.pack()

class PageThree(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text='Graph Page', font = LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1= ttk.Button(self, text='To Start Page',
                        command = lambda: controller.show_frame(StartPage))
        button1.pack()

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side = TOP, fill = BOTH, expand = True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack()

        


app = SeaofBTCapp()
ani = animation.FuncAnimation(f, animate, interval = 250)
app.mainloop()















