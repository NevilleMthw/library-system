from database import Database


class OverdueFines:
    def __init__(self) -> None:
        self.Database = Database()

    def overdue(self) -> str:
        overdue_change = Database.book_Return()
        print(overdue_change)
        return overdue_change

if __name__ == "__main__":
    FINES = OverdueFines()
    FINES.overdue()
