from window import Review
from centerWindow import centerWinodw
from tkinter import Tk


def main():
    root = Tk()
    application = Review()
    window = centerWinodw()
    root.mainloop()

if __name__ == '__main__':
    main()