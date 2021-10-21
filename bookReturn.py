from database import Database

class ReturnBook:
    def __init__(self) -> None:
        self.Database = Database()
    
    def returns(self, book_id_entry1) -> str:
        pass