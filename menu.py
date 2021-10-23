from tkinter import *
import tkinter.scrolledtext as st
import tkinter.ttk as ttk
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import ImageTk, Image
from bookCheckout import CheckoutBook
from bookReturn import ReturnBook


class GUIClass:
    def __init__(self) -> None:
        self.Checkout = CheckoutBook()
        self.Return = ReturnBook()

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

    def checkout(self) -> None:
        global book_img
        global book_id_entry
        book_img = ImageTk.PhotoImage(Image.open("book.jpg"))
        book_img_label = Label(book_checkout, image=book_img)
        book_img_label.pack(side=TOP)
        member_id = Label(
            book_checkout, text="Member ID", font=("Arial", 18), bg="#FEEAE6"
        )
        member_id.pack(padx=400, pady=40, side=TOP)
        member_id_entry = Entry(
            book_checkout, bd=2, bg="Light Blue", justify=CENTER, font=("Arial", 13)
        )
        member_id_entry.pack(side=TOP)
        book_id = Label(book_checkout, text="Book ID", font=("Arial", 18), bg="#FEEAE6")
        book_id.pack(padx=400, pady=40, side=TOP)
        book_id_entry = Entry(
            book_checkout, bd=2, bg="Light Blue", justify=CENTER, font=("Arial", 13)
        )
        book_id_entry.pack(side=TOP)
        book_checkout_button = Button(
            book_checkout,
            text="Book Checkout",
            bg="Light Blue",
            font=("Arial", 13),
            command=lambda: self.Checkout.issue(
                member_id_entry.get(), book_id_entry.get()
            ),
        )
        book_checkout_button.pack(pady=20, side=TOP)

    def checkout_Message(self) -> str:
        pass
        # book_checkout_message:str = Label(book_checkIn, text="Book ID", font=("Arial", 18), bg="#FEEAE6")
        # book_checkout_message.pack()

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
            book_return,
            text="Book Return",
            bg="Light Blue",
            font=("Arial", 13),
            command=lambda: self.Return.returns(book_id_entry.get()),
        )
        book_return_button.pack(pady=20, side=TOP)
    
    def books_Available(self) -> None:
        books_area_heading = Label(dashboard, text='Available Books', font=('Arial', 18))
        books_area_heading.grid(column=0,row=0)
        books_area = st.ScrolledText(dashboard, width=100, height=20)
        books_area.grid(column=0, row=11, rowspan=20)
        books_area.configure(state='disabled')

#####MAIN FUNCTIONS######

window = Tk()
window.title("Library Management System - ADMIN")
window.geometry("1100x580")

tab_control = ttk.Notebook(window)

dashboard = Frame(tab_control, background="#FEEAE6")
tab_control.add(dashboard, text="Dashboard")

book_checkout = Frame(tab_control, background="#FEEAE6")
tab_control.add(book_checkout, text="Book Checkout")

book_return = Frame(tab_control, background="#FEEAE6")
tab_control.add(book_return, text="Book Return")

book_recommendations = Frame(tab_control, background="#FEEAE6")
tab_control.add(book_recommendations, text="Recommendations")

tab_control.pack(expand=1, fill="both")


if __name__ == "__main__":
    GUI = GUIClass()
    GUI.recommendations()
    GUI.checkout()
    GUI.returns()
    GUI.books_Available()

window.mainloop()
