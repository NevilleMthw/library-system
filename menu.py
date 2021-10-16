from tkinter import *
from tkinter import font
import tkinter.ttk as ttk
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import ImageTk, Image


def recommendations() -> None:
    matplotlib.use("TkAgg")
    figure = Figure(figsize=(3, 3), dpi=90)
    plot1 = figure.add_subplot(111)
    plot1.plot(0.5, 0.3, color="blue", marker="o", linestyle="")
    X = [0.2, 0.5, 0.8, 1.0]
    Y = [1.0, 1.2, 1.3, 1.4]
    plot1.plot(X, Y, color="red", marker="x", linestyle="")
    canvas = FigureCanvasTkAgg(figure, master=RECOMMENDATIONS)
    canvas.get_tk_widget().pack()


def checkIn() -> None:
    global BOOK_IMG
    BOOK_IMG = ImageTk.PhotoImage(Image.open('book.jpg'))
    book_Img_label = Label(BOOK_CHECKIN, image=BOOK_IMG)
    book_Img_label.pack(side=TOP)
    member_Id = Label(BOOK_CHECKIN, text='Member ID',
                      font=('Arial', 18), bg='#FEEAE6')
    member_Id.pack(padx=400, pady=40, side=TOP)
    E1 = Entry(BOOK_CHECKIN, bd=2, bg='Light Blue',
               justify=CENTER, font=('Arial', 13))
    E1.pack(side=TOP)
    book_Id = Label(BOOK_CHECKIN, text='Book ID',
                      font=('Arial', 18), bg='#FEEAE6')
    book_Id.pack(padx=400, pady=40, side=TOP)
    E2 = Entry(BOOK_CHECKIN, bd=2, bg='Light Blue',
               justify=CENTER, font=('Arial', 13))
    E2.pack(side=TOP)
    B = Button(BOOK_CHECKIN, text ="Book Check In", bg= 'Light Blue', font=('Arial', 13))
    B.pack(pady=20, side=TOP)

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
checkIn()
WINDOW.mainloop()
