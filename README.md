# library-system

A library management system which has functions for checking in books, returning books and recommendation of books for users. The GUI is robust and provides adequate functionality for basic functions.

1. Functionality guide:
   1. To start the application, one would have to run the python module: `python menu.py`.
   2. After starting the application, three tabs would be present: `Book Checkout`, `Book Return`, `Recommendations`.
   3. To begin working with the application, one would have to input the `member ID` and respective `book ID` which would then checkout the book in the `Book_Info` table and insert into the `Loan_History` table as a transaction.
   4. Once checkout is completed, the user can then return the book by inputting the respective `BookID` in the `book return` tab.
   5. Users can also check the `recommendations` tab where recommendations will be provided based on Genre.
   6. To exit the application, close the window respectively.
2. Elements that could be improved and do not work:
   1. Checkout validation is not present in the application, through interpretation if a bookID is inputted and not present in the `Book_Info` table, this will still add as a transaction in the `Loan_History` but will not change the memberID in the `Book_Info` table.
   2. Overall GUI design could be made more presentable and pleaseing to the eyes.
   3. The calculation of book fines and overdue days could be better suited or placed if done in the `bookCharge` python module instead of a direct SQL query.
   4. Labels or Messageboxes could be used to show once button is clicked for better readability and understanding.
3. Problems faced:
   1. Time management.
   2. Coursework specification understanding.
   3. Unique bugs/errors.
