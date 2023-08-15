from tkinter import Tk,BOTH
from tkinter.ttk import Frame

'''
super() = It calls the parent class’s __init__ method super() to initialize the inherited attribute.
'''
class Example(Frame):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.master.title ("window")
        self.pack(fill=BOTH,expand=1)

def main():
    root = Tk()
    root.geometry("250x150+300+300")
    app = Example()
    root.mainloop()

if __name__ == '__main__':
    main()