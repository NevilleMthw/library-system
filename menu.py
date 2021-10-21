from tkinter import *
import tkinter.ttk as ttk
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import ImageTk, Image
from bookCheckout import CheckoutBook


class GUIClass:
    def __init__(self) -> None:
        self.Checkout = CheckoutBook()

    def recommendations(self) -> None:
        matplotlib.use("TkAgg")
        figure = Figure(figsize=(3, 3), dpi=90)
        plot1 = figure.add_subplot(111)
        plot1.plot(0.5, 0.3, color="blue", marker="o", linestyle="")
        X = [0.2, 0.5, 0.8, 1.0]
        Y = [1.0, 1.2, 1.3, 1.4]
        plot1.plot(X, Y, color="red", marker="x", linestyle="")
        canvas = FigureCanvasTkAgg(figure, master=book_recommendations)
        canvas.get_tk_widget().pack()

    def check_Out(self) -> None:
        global book_img
        global book_id_entry
        book_img = ImageTk.PhotoImage(Image.open("book.jpg"))
        book_img_label = Label(book_checkIn, image=book_img)
        book_img_label.pack(side=TOP)
        member_id = Label(
            book_checkIn, text="Member ID", font=("Arial", 18), bg="#FEEAE6"
        )
        member_id.pack(padx=400, pady=40, side=TOP)
        member_id_entry = Entry(
            book_checkIn, bd=2, bg="Light Blue", justify=CENTER, font=("Arial", 13)
        )
        member_id_entry.pack(side=TOP)
        book_id = Label(book_checkIn, text="Book ID", font=("Arial", 18), bg="#FEEAE6")
        book_id.pack(padx=400, pady=40, side=TOP)
        book_id_entry = Entry(
            book_checkIn, bd=2, bg="Light Blue", justify=CENTER, font=("Arial", 13)
        )
        book_id_entry.pack(side=TOP)
        book_checkIn_button = Button(
            book_checkIn,
            text="Book Checkout",
            bg="Light Blue",
            font=("Arial", 13),
            command=lambda: self.Checkout.issue(book_id_entry),
        )
        book_checkIn_button.pack(pady=20, side=TOP)
        return book_id_entry.get()

    def returns(self) -> None:
        global book_img1
        global book_id_entry1
        book_img1 = ImageTk.PhotoImage(Image.open("book return.jpg"))
        book_img_label1 = Label(book_return, image=book_img1)
        book_img_label1.pack(side=TOP)
        book_id1 = Label(book_return, text="Book ID", font=("Arial", 18), bg="#FEEAE6")
        book_id1.pack(padx=400, pady=40, side=TOP)
        book_id_entry1 = Entry(
            book_return, bd=2, bg="Light Blue", justify=CENTER, font=("Arial", 13)
        )
        book_id_entry1.pack(side=TOP)
        book_return_button = Button(
            book_return, text="Book Return", bg="Light Blue", font=("Arial", 13)
        )
        book_return_button.pack(pady=20, side=TOP)


#####MAIN FUNCTIONS######

window = Tk()
window.title("Library Management System - ADMIN")
window.geometry("1100x580")

tab_control = ttk.Notebook(window)

book_checkIn = Frame(tab_control, background="#FEEAE6")
tab_control.add(book_checkIn, text="Book Checkout")

book_return = Frame(tab_control, background="#FEEAE6")
tab_control.add(book_return, text="Book Return")

book_recommendations = Frame(tab_control, background="#FEEAE6")
tab_control.add(book_recommendations, text="Recommendations")

tab_control.pack(expand=1, fill="both")


if __name__ == "__main__":
    GUI = GUIClass()
    GUI.recommendations()
    GUI.check_Out()
    GUI.returns()

window.mainloop()
