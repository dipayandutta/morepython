from tkinter import BOTH,X,N,LEFT,Text,RIGHT,RAISED
from tkinter.ttk import Frame, Label,Style,Entry,Button


class Review(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("Review System")
        self.style = Style()
        self.style.theme_use("default")
        self.pack(fill=BOTH,expand=True)

        frame1 = Frame(self)
        frame1.pack(fill=X)

        lbl1 = Label(frame1,text="Title",width=6)
        lbl1.pack(side=LEFT,padx=5,pady=5)

        entry1 = Entry(frame1)
        entry1.pack(fill=X,padx=5,expand=True)

        frame2 = Frame(self)
        frame2.pack(fill=X)

        lbl2 = Label(frame2, text="Author", width=6)
        lbl2.pack(side=LEFT, padx=5, pady=5)

        entry2 = Entry(frame2)
        entry2.pack(fill=X, padx=5, expand=True)

        frame3 = Frame(self)
        frame3.pack(fill=BOTH, expand=True)

        lbl3 = Label(frame3, text="Review", width=6)
        lbl3.pack(side=LEFT, anchor=N, padx=5, pady=5)

        txt = Text(frame3)
        txt.pack(fill=BOTH, pady=5, padx=5, expand=True)


       

