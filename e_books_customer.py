import hashlib
import uuid
import bcrypt
from e_books_connect import MSDBConnection


class DBClientTable(MSDBConnection):

    def create_client(self, customer_id, email_address, contact_f_name, contact_l_name, contact_title, address, city,
                      region, postal_code, country, phone, _password_hash):
        salt = uuid.uuid4().hex
        hashing_password = hashlib.sha512(_password_hash + salt).hexdigest()
        return self.sql_query(f"""INSERT INTO Customers (CustomerID, CompanyName, ContactName, ContactTitle, Address,
                                   City, Region, PostalCode, Country, Phone) VALUES ('{customer_id}',  
                                   '{email_address}', '{contact_f_name}', '{contact_l_name} '{contact_title}', 
                                   '{address}', '{city}', '{region}', '{postal_code}', '{country}', '{phone}', 
                                   '{_password_hash}')""").commit

    def _create_password(self, new_password):
        self._password_hash = new_password
        return bcrypt.hashpw(new_password, bcrypt.gensalt())

    @staticmethod
    def check_password(new_password, hashed_password):
        count = 3
        while new_password != hashed_password:
            count -= 1
            if count == 2:
                return 'you have two more attempts remaining'
            if count == 1:
                return 'you have one more attempt remaining'
            while count <= 0:
                return """too many attempts. Closing program. Please contact another administrator. As an administrator 
                                  with responsibility over passwords it does not look good that you forgot your password"""
        return bcrypt.checkpw(new_password, hashed_password)



    # def _create_password(self, new_password):
    #     self._password = new_password
    #     return new_password
    #
    # def get_password(self):
    #     return self._password
    #
    # def check_password(self, enter_password):
    #     count = 3
    #     query_1 = self.sql_query(enter_password)
    #     query_2 = self.sql_query() # check password against existing record)
    #     while query_1 != query_2:
    #         count -= 1
    #         if count == 2:
    #             return 'you have two more attempts remaining'
    #         if count == 1:
    #             return 'you have one more attempt remaining'
    #         while count <= 0:
    #             return 'too many attempts. Closing program. Please contact administrator'

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


