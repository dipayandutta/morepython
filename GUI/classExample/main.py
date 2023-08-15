from window import Buttons
from centerWindow import centerWindow
from tkinter import Tk 

def main():
    root = Tk()
    application = Buttons()
    window = centerWindow()
    root.mainloop()

if __name__ =='__main__':
    main()