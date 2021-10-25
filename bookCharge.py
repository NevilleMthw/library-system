from database import Database


class OverdueFines:
    """This class returns the overdue table."""
    def __init__(self) -> None:
        """Initializing the database class to use the functions from that python module."""
        self.Database = Database()

    def overdue(self) -> str:
        overdue_change = self.Database.book_Return()
        print(overdue_change)
        return overdue_change

if __name__ == "__main__":
    FINES = OverdueFines()
    FINES.overdue()
