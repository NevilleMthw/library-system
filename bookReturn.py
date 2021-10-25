from database import Database


class ReturnBook:
    """
    This class returns the result with the bookID,
    thereby checking the bookID entry and performing the respective functions.
    """

    def __init__(self) -> None:
        """Initializing the database class to use the functions from that python module."""
        self.Database = Database()

    def returns(self, book_id_entry: str) -> str:
        """
        This function checks whether the bookID entered is right for the return.
        @param book_id_entry: Will take the BookID input.
        """
        return_result = self.Database.book_Return(book_id_entry)
        if book_id_entry == return_result:
            print("This works")


if __name__ == "__main__":
    R_BOOK = ReturnBook()
    R_BOOK.returns()
