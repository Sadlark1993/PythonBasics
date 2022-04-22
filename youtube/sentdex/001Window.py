from tkinter import *

class Window(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)

        self.master = master

        self.init_window()

    def init_window(self):
        self.master.title("GUI")
        self.pack(fill=BOTH, expand=1)

        my_menu = Menu(self.master)
        self.master.config(menu=my_menu)

        file = Menu(my_menu)
        file.add_command(label='Save')
        file.add_command(label='Exit', command = lambda: exit())
        my_menu.add_cascade(label='File', menu=file)

        edit = Menu(my_menu)
        edit.add_command(label='Undo')
        my_menu.add_cascade(label='Edit', menu = edit)

root = Tk()
root.geometry("400x300")
app = Window(root)
root.mainloop()
