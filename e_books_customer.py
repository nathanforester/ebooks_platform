from e_books_connect import MSDBConnection

class DBClientTable(MSDBConnection):

    def create_client(self, customer_id, email_address, contact_f_name, contact_l_name, contact_title, address, city,
                      region, postal_code, country, phone, _password):
        return self.sql_query(f"""INSERT INTO Customers (CustomerID, CompanyName, ContactName, ContactTitle, Address,
                                   City, Region, PostalCode, Country, Phone, Fax) VALUES ('{customer_id}',  
                                   '{email_address}', '{contact_f_name}', '{contact_l_name} '{contact_title}', 
                                   '{address}', '{city}', '{region}', '{postal_code}', '{country}', '{phone}', 
                                   '{_password}')""").commit

    def _create_password(self, new_password):
        self._password = new_password
        return new_password

    def get_password(self):
        return self._password

    def check_password(self, enter_password):
        count = 3
        query_1 = self.sql_query(enter_password)
        query_2 = self.sql_query() # check password against existing record)
        while query_1 != query_2:
            count -= 1
            if count == 2:
                return 'you have two more attempts remaining'
            if count == 1:
                return 'you have one more attempt remaining'
            while count <= 0:
                return 'too many attempts. Closing program. Please contact administrator'

    # def get_by_id(self, val):
    #     return self.sql_query(str(f"SELECT * FROM Customers WHERE CustomerID = {val}")).fetchall()
    #
    # def get_all(self, name=None):
    #     result_list = []
    #     if name is None:
    #         query_result = self.sql_query('SELECT * FROM Customers')
    #     else:
    #         query_result = self.sql_query(f"SELECT * FROM Customers WHERE ContactName LIKE '%{name}%'")
    #     while True:
    #         row = query_result.fetchone()
    #         if row is None:
    #             break
    #         result_list.append(row)
    #     return result_list


