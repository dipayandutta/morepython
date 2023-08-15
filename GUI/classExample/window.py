from tkinter import RIGHT,BOTH,RAISED
from tkinter.ttk import Frame,Button,Style
from printText import printText
from Quit import Quit

class Buttons(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()
        

    def initUI(self):
        self.master.title("Main Window")
        self.style = Style()
        self.style.theme_use("default")

        frame = Frame(self,relief=RAISED,borderwidth=1)
        frame.pack(fill=BOTH,expand=True)

        self.pack(fill=BOTH,expand=True)

        closeButton = Button(self,text='Close',command=lambda: Quit.close())
        closeButton.pack(side=RIGHT,padx=5,pady=5)

        okButton = Button(self,text='OK',command=lambda: printText.okButtonPressed())
        okButton.pack(side=RIGHT)



   