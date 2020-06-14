from e_books_connect import MSDBConnection

nwind = MSDBConnection()


class DbBookTable(MSDBConnection):

    def create_entry(self, book_id, book_name, author, genre, isbn):
        return self.sql_query(f"""INSERT INTO Books (BookName, Author, Genre, ISBN)
                               VALUES ('{book_name}', {author}, {genre}, '{isbn}')""").commit

    def get_by_id(self, ids):
        return self.sql_query(f"SELECT * FROM Books WHERE BookID = " + str(ids)).fetchone()

    def get_all(self, product_name=None):
        result_list = []
        if product_name is None:
            query_result = self.sql_query('SELECT * FROM Books')
        else:
            query_result = self.sql_query(f"SELECT * FROM Books WHERE Book LIKE '%{product_name}%'")
        while True:
            row = query_result.fetchone()
            if row is None:
                break
            result_list.append(row)
        return result_list

    def _insert_into(self, val_1, val_2, val_3):
        self.new_insert = self.sql_query(f"""INSERT INTO Books (BookName, Author, Genre) VALUES ('{val_1}', '{val_2}', 
                                         '{val_3}';""").commit
        return self.new_insert

    def get_insert(self):
        return self.new_insert

    def _create_book(self, val_1, val_2):
        self.create_new = self.sql_query(f"""INSERT INTO BookContents (BookName, Text) VALUES ('{val_1}', 
                                         '{val_2};""").commit
        return self.create_new

    def get_create_book(self):
        return self.create_new

    def _update_book(self, new_book_name):
        self.book_name = new_book_name
        new_book_name = open(f"{new_book_name}", "a")
        return new_book_name.write('')






