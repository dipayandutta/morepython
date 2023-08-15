from tkinter.ttk import Frame

class centerWindow(Frame):
     
     def __init__(self):
         super().__init__()
         self.windowGeometry()
     
     def windowGeometry(self):
        width = 290
        height= 150

        sw = self.master.winfo_screenwidth()
        sh = self.master.winfo_screenheight()

        x = (sw-width)/2
        y = (sh-height)/2

        self.master.geometry('%dx%d+%d+%d'%(width,height,x,y))

