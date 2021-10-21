import sqlite3
import csv


class Database:
    def __init__(self) -> None:

        self.connection = sqlite3.connect("Library.db")
        self.cursor = self.connection.cursor()

    def populate_DB(self) -> str:
        self.connection = sqlite3.connect("Library.db")
        self.cursor = self.connection.cursor()
        try:
            self.cursor.execute(
                "CREATE TABLE IF NOT EXISTS Book_Info (ID PRIMARY KEY, Genre, Title, Author, LoanPeriod, PurchaseDate, Memberid)"
            )
            self.cursor.execute(
                "CREATE TABLE IF NOT EXISTS Loan_History (TransactionID PRIMARY KEY, BookID, CheckoutDate, ReturnDate)"
            )
            with open("Book_Info.txt") as file_open:
                for row in csv.reader(file_open, delimiter=","):
                    self.cursor.execute(
                        "INSERT INTO Book_Info VALUES (:ID, :Genre, :Title, :Author, :LoanPeriod, :PurchaseDate, :Memberid)",
                        row,
                    )
            file_open.close()
            with open("Loan_History.txt") as file_open1:
                for row in csv.reader(file_open1, delimiter=","):
                    self.cursor.execute(
                        "INSERT INTO Loan_History VALUES (:TransactionID, :BookID, :CheckoutDate, :ReturnDate)",
                        row,
                    )
            file_open1.close()
            self.connection.commit()
            self.connection.close()
        except Exception as e:
            print(e)

    def book_Retrieval(self) -> str:
        connection = sqlite3.connect("Library.db")
        cursor = connection.cursor()
        result = cursor.execute("SELECT Memberid, ID FROM Book_Info")
        connection.commit()
        return result

    def book_Return(self) -> str:
        connection = sqlite3.connect("Library.db")
        cursor = connection.cursor()
        result = cursor.execute(
            "INSERT INTO Loan_History VALUES (:TransactionID, :BookID, :CheckoutDate, :ReturnDate)"
        )
        connection.commit()
        return result

    def DB_Close_Connection(self) -> None:
        self.connection.close()


if __name__ == "__main__":
    DB = Database()
    DB.populate_DB()
    DB.book_Retrieval()
    # DB.book_Return()
    DB.DB_Close_Connection()
