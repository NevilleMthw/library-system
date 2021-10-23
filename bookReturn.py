from database import Database


class ReturnBook:
    def __init__(self) -> None:
        self.Database = Database()
        # self.Date = date()

    def returns(self, book_id_entry: str) -> str:
        return_result = self.Database.book_Return(book_id_entry)
        if book_id_entry == return_result:
            print("This works")


if __name__ == "__main__":
    R_BOOK = ReturnBook()
    R_BOOK.returns()
