from tkinter import Tk,BOTH,RIGHT , RAISED
from tkinter.ttk import Frame,Button,Style


class Buttons(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("Buttons Layout")
        self.style = Style()
        self.style.theme_use("default")

        frame = Frame(self,relief=RAISED,borderwidth=1)
        frame.pack(fill=BOTH,expand=True)

        self.pack(fill=BOTH,expand=True)

        closeButton=Button(self,text="Close",command=self.quit)
        closeButton.pack(side=RIGHT,padx=5,pady=5)

        okBUtton = Button(self,text="OK",command=self.printText)
        okBUtton.pack(side=RIGHT)

        self.centerWindow()

    def printText(self):
        print("Ok Button Pressed!")

    def centerWindow(self):
        width = 290 
        height= 150

        sw = self.master.winfo_screenwidth()
        sh = self.master.winfo_screenheight()

        x = (sw-width)/2
        y = (sh -height)/2

        self.master.geometry('%dx%d+%d+%d'%(width,height,x,y))


def main():
    root =Tk()
    app = Buttons()
    root.mainloop()

if __name__ == '__main__':
    main()