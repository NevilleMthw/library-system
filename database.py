import sqlite3
import csv
from datetime import datetime


class Database:
    def populate_DB(self) -> None:
        self.connection = sqlite3.connect("Library.db")
        self.connection.execute("pragma journal_mode=wal")
        self.cursor = self.connection.cursor()
        with self.connection:
            try:
                self.cursor.execute(
                    "CREATE TABLE IF NOT EXISTS Book_Info (ID PRIMARY KEY, Genre, Title, Author, LoanPeriod, PurchaseDate, CurrentLoanStatus)"
                )
                self.cursor.execute(
                    "CREATE TABLE IF NOT EXISTS Loan_History (TransactionID INTEGER PRIMARY KEY AUTOINCREMENT, BookID, CheckoutDate DATETIME default CURRENT_DATE, ReturnDate)"
                )
                with open("Book_Info.txt") as file_open:
                    for row in csv.reader(file_open, delimiter=","):
                        self.cursor.execute(
                            "INSERT INTO Book_Info VALUES (:ID, :Genre, :Title, :Author, :LoanPeriod, :PurchaseDate, :CurrentLoanStatus)",
                            row,
                        )
                with open("Loan_History.txt") as file_open1:
                    for row in csv.reader(file_open1, delimiter=","):
                        self.cursor.execute(
                            "INSERT INTO Loan_History VALUES (:TransactionID, :BookID, :CheckoutDate,:ReturnDate)",
                            row,
                        )
                file_open1.close()
                self.connection.commit()
            except Exception as e:
                print(e)

    def book_MemberID_Change(self, member_id_entry: str, book_id_entry: str) -> str:
        with sqlite3.connect("Library.db", isolation_level=None) as connection:
            cursor = connection.cursor()
            connection.execute("pragma journal_mode=wal")
            result = cursor.execute(
                "UPDATE Book_Info SET CurrentLoanStatus = ? WHERE ID = ?",
                (member_id_entry, book_id_entry,),
            )
            result1 = cursor.execute(
                "INSERT INTO Loan_History (BookID) VALUES (?)", (book_id_entry,)
            )
            connection.commit()
            return result.fetchall(), result1.fetchall()

    def book_Return(self, book_id_entry) -> None:
        with sqlite3.connect("Library.db", isolation_level=None) as connection:
            return_date = datetime.now().strftime("%m-%d-%Y")
            cursor = connection.cursor()
            connection.execute("pragma journal_mode=wal")
            result = cursor.execute(
                "UPDATE Loan_History SET ReturnDate = ? WHERE BookID = ? AND ReturnDate IS NULL",
                (
                    return_date,
                    book_id_entry,
                ),
            )
            connection.commit()
            return result.fetchall()
    
    def book_Charge(self) -> None:
        with sqlite3.connect("Library.db", isolation_level=None) as connection:
            return_date = datetime.now().strftime("%m-%d-%Y")
            cursor = connection.cursor()
            connection.execute("pragma journal_mode=wal")
            result = cursor.execute(
                "UPDATE Loan_History SET ReturnDate = ? WHERE BookID = ? AND ReturnDate IS NULL",
                (
                    return_date,
                ),
            )
            connection.commit()
            return result.fetchall()

if __name__ == "__main__":
    DB = Database()
    DB.populate_DB()
