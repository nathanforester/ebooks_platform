from e_books_connect import MSDBConnection

nwind = MSDBConnection()


class DbBookTable(MSDBConnection):

    def create_entry(self, book_id, book_name, author, genre, isbn):
        return self.sql_query(f"""INSERT INTO Books (BookName, Author, Genre, ISBN)
                               VALUES ('{book_name}', {author}, {genre}, '{isbn}')""").commit

    def get_by_id(self, ids):
        return self.sql_query(f"SELECT * FROM Products WHERE ProductID = " + str(ids)).fetchone()

    def get_all(self, product_name=None):
        result_list = []
        if product_name is None:
            query_result = self.sql_query('SELECT * FROM Products')
        else:
            query_result = self.sql_query(f"SELECT * FROM Products WHERE ProductName LIKE '%{product_name}%'")
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


class CRUDRecord(DbBookTable):

    new_record = DbBookTable().get_by_id(id)


