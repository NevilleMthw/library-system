from database import Database


class CheckoutBook:
    def __init__(self) -> None:
        self.Database = Database()

    def issue(self, member_id_entry: str, book_id_entry: str) -> str:
        issue_id_change = self.Database.book_MemberID_Change(
            member_id_entry, book_id_entry
        )
        data = issue_id_change
        y = len(data)
        for x in range(0, y):
            if book_id_entry and member_id_entry == data:
                print(issue_id_change)


if __name__ == "__main__":
    CHKOUT_BOOK = CheckoutBook()
    CHKOUT_BOOK.issue()
