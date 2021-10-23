import sqlite3
import csv


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
                    "CREATE TABLE IF NOT EXISTS Loan_History (TransactionID INTEGER PRIMARY KEY AUTOINCREMENT, BookID, CheckoutDate DATETIME default CURRENT_DATE, ReturnDate DATETIME)"
                )
                with open("Book_Info.txt") as file_open:
                    for row in csv.reader(file_open, delimiter=","):
                        self.cursor.execute(
                            "INSERT INTO Book_Info VALUES (:ID, :Genre, :Title, :Author, :LoanPeriod, :PurchaseDate, :CurrentLoanStatus)",
                            row,
                        )
                self.connection.commit()
            except Exception as e:
                print(e)

    def book_Retrieval(self) -> str:
        with sqlite3.connect("Library.db", isolation_level=None) as connection:
            cursor = connection.cursor()
            connection.execute("pragma journal_mode=wal")
            result = cursor.execute("SELECT CurrentLoanStatus, ID FROM Book_Info")
            connection.commit()
            return result

    def book_MemberID_Change(self, member_id_entry: str, book_id_entry: str) -> str:
        with sqlite3.connect("Library.db", isolation_level=None) as connection:
            cursor = connection.cursor()
            connection.execute("pragma journal_mode=wal")
            result = cursor.execute("SELECT CurrentLoanStatus, ID FROM Book_Info")
            result1 = cursor.execute(
                f"UPDATE Book_Info SET CurrentLoanStatus = '{member_id_entry}' WHERE ID = '{book_id_entry}'"
            )
            # result1 = cursor.execute(
            #     "UPDATE Book_Info SET CurrentLoanStatus = ? WHERE ID = ?", (member_id_entry,book_id_entry)
            # )
            result2 = cursor.execute(
                f"INSERT INTO Loan_History (BookID) VALUES ('{book_id_entry}')"
            )
            connection.commit()
            return result.fetchall(), result1.fetchall(), result2.fetchall()

    def book_Return(self, checkout_date, return_date, book_id_entry) -> None:
        with sqlite3.connect("Library.db", isolation_level=None) as connection:
            cursor = connection.cursor()
            connection.execute("pragma journal_mode=wal")
            result = cursor.execute(
                f"""UPDATE Loan_History SET ReturnDate = '{return_date}'  WHERE BookID = '{book_id_entry}'"""
            )
            connection.commit()
            return result


if __name__ == "__main__":
    DB = Database()
    DB.populate_DB()
    # DB.book_Return()
