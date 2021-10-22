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
                    "CREATE TABLE IF NOT EXISTS Loan_History (TransactionID PRIMARY KEY, BookID, CheckoutDate, ReturnDate)"
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
                            "INSERT INTO Loan_History VALUES (:TransactionID, :BookID, :CheckoutDate, :ReturnDate)",
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
            result = cursor.execute(
                f"""UPDATE Book_Info SET CurrentLoanStatus = '{member_id_entry}' WHERE ID = '{book_id_entry}'"""
            )
            connection.commit()
            return result

    def book_Return(self) -> None:
        connection = sqlite3.connect("Library.db")
        cursor = connection.cursor()
        result = cursor.execute(
            "INSERT INTO Loan_History (TransactionID, BookID, CheckoutDate, ReturnDate)"
        )
        connection.commit()
        connection.close()
        return result


if __name__ == "__main__":
    DB = Database()
    DB.populate_DB()
    # DB.book_MemberID_Change('anan', 'A1')
