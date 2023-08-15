from tkinter import Tk,BOTH
from tkinter.ttk import Frame, Button ,Style

class QuitButton(Frame):
    def __init__(self):
        super().__init__()
        
        #UI initialization
        self.initUI()

    def initUI(self):
        self.master.title("Quit Button Example")
        # set theme
        self.style = Style()
        self.style.theme_use("default")

        self.pack(fill=BOTH,expand=1)

        # Creating the Quit Button
        quitButton = Button(self,text="Quit",command=self.quit)
        quitButton.place(x=50,y=50)

        self.centerWindow()

    def centerWindow(self):
        width = 290 
        height= 150

        sw = self.master.winfo_screenwidth()
        sh = self.master.winfo_screenheight()

        x = (sw-width)/2
        y = (sh -height)/2

        self.master.geometry('%dx%d+%d+%d'%(width,height,x,y))

def main():
    root = Tk()
    app = QuitButton()
    root.mainloop()

if __name__ == '__main__':
    main()