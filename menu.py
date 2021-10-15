from tkinter import *
import tkinter.ttk as ttk
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def createTabBar() -> None:
    # Create Tab Control
    TAB_CONTROL = ttk.Notebook(WINDOW)

    RECOMMENDATIONS = Frame(TAB_CONTROL, background='#FEEAE6')
    TAB_CONTROL.add(RECOMMENDATIONS, text='Recommendations')

    BOOK_RETURN = Frame(TAB_CONTROL, background='#FEEAE6')
    TAB_CONTROL.add(BOOK_RETURN, text='Book Return')
    BOOK_CHECKIN = Frame(TAB_CONTROL, background='#FEEAE6')
    TAB_CONTROL.add(BOOK_CHECKIN, text='Book CheckIn')

    TAB_CONTROL.pack(expand=1, fill="both")


def recommendations() -> None:
    matplotlib.use("TkAgg")
    TAB_CONTROL = ttk.Notebook(WINDOW)
    RECOMMENDATIONS = Frame(TAB_CONTROL)
    TAB_CONTROL.add(RECOMMENDATIONS, text='Recommendations')
    figure = Figure(figsize=(3, 3), dpi=90)
    plot1 = figure.add_subplot(111)
    plot1.plot(0.5, 0.3, color="blue", marker="o", linestyle="")
    x = [0.2,0.5,0.8,1.0 ]
    y = [ 1.0, 1.2, 1.3,1.4]
    plot1.plot(x, y, color="red", marker="x", linestyle="")
    canvas = FigureCanvasTkAgg(figure, WINDOW)
    canvas.get_tk_widget().pack()

#####MAIN FUNCTIONS######
WINDOW = Tk()
WINDOW.title("Library Management System - ADMIN")
WINDOW.geometry('1100x580')

createTabBar()
recommendations()
WINDOW.mainloop()
