from e_books_admin import DBCAdminTable
from e_books_customer import DBClientTable
from e_books_products_and_records import DbBookTable

new_admin = DBCAdminTable()
new_customer = DBClientTable()
new_book = DbBookTable

while True:
    user_input = input("""Welcome to Forester's free for all ebook store. Push any key to continue or 'x' to exit. 
                       Admin login please push a: """)
    while user_input != 'x':
        if user_input == 'a':
            user_input_1 = input("please enter your username: ")
            user_input_2 = input("please enter your password: ")
            # need function call for checking password and if password is correct, continue to next block of code
        elif user_input != 'a':
            user_input_1 = input("please enter your username: ")
            user_input_2 = input("please enter your password: ")
            # need function call for checking password and if password is correct, continue to next block of code
            # next block of code will be quite extensive, giving access to many administrator functions
        # if password correct, then:
            user_input_1 = input("please choose s to search for a book or a to add a new book: ")
            if user_input_1 == 's':
                # method call search function from user input
                # EXTRA: method call to allow user to return to main menu
            elif user_input_1 == 'a':
                # method call add function from user input
                # here, users can request books t
            # add another input to ask for further search/insertions, or to exit

