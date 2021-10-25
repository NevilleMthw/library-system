from database import Database


class CheckoutBook:
    """This class returns the issue function where the bookID is validated to check the data in the DB."""

    def __init__(self) -> None:
        """Initializing the database class to use the functions from that python module."""
        self.Database = Database()

    def issue(self, member_id_entry: str, book_id_entry: str) -> str:
        issue_id_change = self.Database.book_MemberID_Change(
            member_id_entry, book_id_entry
        )
        data = issue_id_change
        y = len(data)
        for x in range(0, y):
            if book_id_entry == data:
                print("Book issued successfully!")


if __name__ == "__main__":
    CHKOUT_BOOK = CheckoutBook()
    CHKOUT_BOOK.issue()
