from e_books_connect import MSDBConnection


class DBCAdminTable(MSDBConnection):

    def _create_admin(self, customer_id, CompanyName, ContactName, ContactTitle, Address, City, Region, PostalCode,
                      Country, Phone, Fax):
        self.new_add = self.sql_query(f"""INSERT INTO Customers (CustomerID, CompanyName, ContactName, ContactTitle, Address,
                                   City, Region, PostalCode, Country, Phone, Fax) VALUES ('{customer_id}',  
                                   '{CompanyName}', '{ContactName}', '{ContactTitle}', '{Address}', '{City}', '{Region}', 
                                   '{PostalCode}', '{Country}', '{Phone}', '{Fax}')""").commit
        return self.new_add

    def get_create_admin(self):
        return self.new_add

    def get_by_id(self, val):
        return self.sql_query(str(f"SELECT * FROM Customers WHERE CustomerID = '{val}'")).fetchall()

    def get_all(self, client_name=None):
        result_list = []
        if client_name is None:
            query_result = self.sql_query('SELECT * FROM Customers')
        else:
            query_result = self.sql_query(f"SELECT * FROM Customers WHERE ContactName LIKE '%{client_name}%'")
        while True:
            row = query_result.fetchone()
            if row is None:
                break
            result_list.append(row)
        return result_list

    def _create_table(self):
        pass

    def get_create_table(self):
        pass

    def _drop_table(self):
        pass

    def get_drop_table(self):
        pass

    def _del_record(self):
        pass

    def get_del_record(self):
        pass

    def _update_db(self, column_1, val_1, column_2, condition):
        self.update = self.sql_query(f"UPDATE Products SET {column_1} = '{val_1}' WHERE {column_2} = '{condition}'").commit
        return self.update

    def get_update_db(self):
        return self.update


