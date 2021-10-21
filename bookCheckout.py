from database import Database


class CheckoutBook:
    def __init__(self) -> None:
        self.Database = Database()

    def issue(self, book_id_entry) -> str:
        result = self.Database.book_Retrieval()
        print("HELLO THIS IS WORKING.")

        if book_id_entry == result.fetchall()[0][1]:
            print("great")


if __name__ == "__main__":
    CHBOOK = CheckoutBook()
    CHBOOK.issue("A1")
