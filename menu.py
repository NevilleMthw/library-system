from tkinter import *
import tkinter.ttk as ttk
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def recommendations() -> None:
    matplotlib.use("TkAgg")
    figure = Figure(figsize=(3, 3), dpi=90)
    plot1 = figure.add_subplot(111)
    plot1.plot(0.5, 0.3, color="blue", marker="o", linestyle="")
    x = [0.2, 0.5, 0.8, 1.0]
    y = [1.0, 1.2, 1.3, 1.4]
    plot1.plot(x, y, color="red", marker="x", linestyle="")
    canvas = FigureCanvasTkAgg(figure, master=RECOMMENDATIONS)
    canvas.get_tk_widget().pack()

#####MAIN FUNCTIONS######


WINDOW = Tk()
WINDOW.title("Library Management System - ADMIN")
WINDOW.geometry('1100x580')

TAB_CONTROL = ttk.Notebook(WINDOW)

BOOK_CHECKIN = Frame(TAB_CONTROL, background='#FEEAE6')
TAB_CONTROL.add(BOOK_CHECKIN, text='Book CheckIn')

BOOK_RETURN = Frame(TAB_CONTROL, background='#FEEAE6')
TAB_CONTROL.add(BOOK_RETURN, text='Book Return')

RECOMMENDATIONS = Frame(TAB_CONTROL, background='#FEEAE6')
TAB_CONTROL.add(RECOMMENDATIONS, text='Recommendations')


TAB_CONTROL.pack(expand=1, fill="both")

recommendations()

WINDOW.mainloop()
