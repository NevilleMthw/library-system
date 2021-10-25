import sqlite3
import csv
from datetime import datetime


class Database:
    """This class contains image read and write functions along with population of database,
    updation of tables and insert queries for each use case.
    All SQLite queries are being run in this python module.
    """

    def __init__(self) -> None:
        """Connection to database, along with context managers (WAL: Write-Ahead Logging) to prevent database lockout.
        Creation of tables are being executed within the exception handling test case.
        """
        self.connection = sqlite3.connect("Library.db")
        self.connection.execute("pragma journal_mode=wal")
        self.cursor = self.connection.cursor()
        with self.connection:
            try:
                self.cursor.execute(
                    "CREATE TABLE IF NOT EXISTS Book_Info (ID PRIMARY KEY, Genre, Title, Author, LoanPeriod, PurchaseDate, CurrentLoanStatus)"
                )
                self.cursor.execute(
                    "CREATE TABLE IF NOT EXISTS Loan_History (TransactionID INTEGER PRIMARY KEY AUTOINCREMENT, BookID, CheckoutDate DATETIME default CURRENT_DATE, ReturnDate DATE DEFAULT NULL)"
                )
                self.cursor.execute(
                    "CREATE TABLE IF NOT EXISTS Overdue_Books (BookID PRIMARY KEY, CurrentLoanStatus, CheckoutDate DATETIME default CURRENT_DATE, ReturnDate, Fines REAL, OverdueDays DATETIME)"
                )
                self.cursor.execute(
                    "CREATE TABLE IF NOT EXISTS Image_Data (Photo BLOB NOT NULL)"
                )
                self.connection.commit()
            except Exception as e:
                print(e)
            finally:
                self.populate_DB()

    # Converting digital data to binary format
    def convert_Image(self, photo):
        with open(photo, "rb") as books_img:
            img_data = books_img.read()
        books_img.close()
        return img_data

    # Connecting to database where image is being read as bytes and then inserted as a tuple.
    def insert_Image(self, book):
        try:
            self.connection = sqlite3.connect("Library.db")
            self.connection.execute("pragma journal_mode=wal")
            self.cursor = self.connection.cursor()
            print("Connected to SQLite")
            bookImg = self.convert_Image(book)
            data_tuple = bookImg
            self.cursor.execute(
                "INSERT INTO Image_Data (Photo) VALUES (?)", [data_tuple]
            )
            self.connection.commit()
            print("Image uploaded")
        except sqlite3.Error as e:
            print(e)
        finally:
            if self.connection:
                self.connection.close()
                print("FINISHED.")

    # Convert binary data to proper format
    def write_Img(self, data, filename):
        with open(filename, "wb") as file:
            file.write(data)

    # Retrieve the image as BLOB data type and write onto the hard drive.
    def write_Img_Data(self):
        try:
            global r_data
            r_data = ""
            self.connection = sqlite3.connect("Library.db")
            self.connection.execute("pragma journal_mode=wal")
            self.cursor = self.connection.cursor()
            print("Connected to SQLite")
            select_books = "SELECT * FROM Image_Data"
            data = self.cursor.execute(select_books)
            for x in data:
                r_data = x[0]
                photo_path = "book.jpg"
                photo_path1 = "book return.jpg"
                self.write_Img(r_data, photo_path)
                self.write_Img(r_data, photo_path1)
            self.connection.commit()
        except sqlite3.Error as e:
            print(e)
        finally:
            if self.connection:
                self.connection.close()
                print("sqlite connection is closed")

    def populate_DB(self) -> None:
        try:
            with open("Book_Info.txt") as file_open:
                for row in csv.reader(file_open, delimiter=","):
                    self.cursor.execute(
                        "INSERT or IGNORE INTO Book_Info VALUES (:ID, :Genre, :Title, :Author, :LoanPeriod, :PurchaseDate, :CurrentLoanStatus)",
                        row,
                    )
            file_open.close()
            with open("Loan_History.txt") as file_open1:
                for row in csv.reader(file_open1, delimiter=","):
                    self.cursor.execute(
                        "INSERT or IGNORE INTO Loan_History VALUES (:TransactionID, :BookID, :CheckoutDate,:ReturnDate)",
                        row,
                    )
            file_open1.close()
        except Exception as e:
            print(e)

    # This function would work during the checkout phase which would update the Book_Info table then insert to the Loan_History and Overdue_Books.
    def book_MemberID_Change(self, member_id_entry: str, book_id_entry: str) -> str:
        with sqlite3.connect("Library.db", isolation_level=None) as connection:
            cursor = connection.cursor()
            connection.execute("pragma journal_mode=wal")
            result = cursor.execute(
                "UPDATE Book_Info SET CurrentLoanStatus = ? WHERE ID = ?",
                (
                    member_id_entry,
                    book_id_entry,
                ),
            )
            result1 = cursor.execute(
                "INSERT INTO Loan_History (BookID) VALUES (?)", (book_id_entry,)
            )
            result2 = cursor.execute(
                "INSERT INTO Overdue_Books (BookID, CurrentLoanStatus) VALUES (?, ?)",
                (
                    book_id_entry,
                    member_id_entry,
                ),
            )
            connection.commit()
            return result.fetchall(), result1.fetchall(), result2.fetchall()

    # This function would update the Loan_History table which would then go onto the Overdue_Books update, 
    # where the overdue days and fines are bein calculated through SQL query using JULIANDAY conversion.
    def book_Return(self, book_id_entry: str) -> None:
        with sqlite3.connect("Library.db", isolation_level=None) as connection:
            return_date = datetime.now().strftime("%Y-%m-%d")
            fine_amount = 0.25
            cursor = connection.cursor()
            connection.execute("pragma journal_mode=wal")
            result = cursor.execute(
                "UPDATE Loan_History SET ReturnDate = ? WHERE BookID = ? AND ReturnDate IS NULL",
                (
                    return_date,
                    book_id_entry,
                ),
            )
            result1 = cursor.execute(
                "UPDATE Overdue_Books SET ReturnDate = ? ,OverdueDays = CAST(JULIANDAY(?) - (SELECT JULIANDAY(t.CheckoutDate) FROM Overdue_Books t WHERE t.BookID = Overdue_Books.BookID) AS INTEGER) ,Fines = ? * CAST(JULIANDAY(?) - (SELECT JULIANDAY(t.CheckoutDate) FROM Overdue_Books t WHERE t.BookID = Overdue_Books.BookID) AS INTGER) WHERE BookID = ?",
                (
                    return_date,
                    return_date,
                    fine_amount,
                    return_date,
                    book_id_entry,
                ),
            )
            connection.commit()
            return result.fetchall(), result1.fetchall()


if __name__ == "__main__":
    DB = Database()
    DB.write_Img_Data()
    DB.write_Img_Data()
