from tkinter import *
from tkinter.ttk import *

def createTabBar():
    #Create Tab Control
    TAB_CONTROL = Notebook(WINDOW)

    RECOMMENDATIONS = Frame(TAB_CONTROL)
    TAB_CONTROL.add(RECOMMENDATIONS, text='Recommendations')

    BOOK_RETURN = Frame(TAB_CONTROL)
    TAB_CONTROL.add(BOOK_RETURN, text='Book Return')
    BOOK_CHECKIN = Frame(TAB_CONTROL)
    TAB_CONTROL.add(BOOK_CHECKIN, text='Book CheckIn')

    TAB_CONTROL.pack(expand=1, fill="both")

WINDOW = Tk()
WINDOW.title("Library Management System - ADMIN") 
WINDOW.geometry('1100x580')

createTabBar()
WINDOW.mainloop()


