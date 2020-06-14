from e_books_connect import MSDBConnection


class DBCAdminTable(MSDBConnection):

    def _create_admin(self, admin_id, department, email, admin_f_name, admin_l_name, address, city, region, postal_code,
                      country, phone):
        self.new_add = self.sql_query(f"""INSERT INTO Administrators (AdminID, Department, AdminFName, Admin_l_name, 
                                      ContactTitle, Address, City, Region, PostalCode, Country, Phone, Fax) 
                                      VALUES ({admin_id},'{department}', '{email}', '{admin_f_name}', '{admin_l_name}', 
                                      '{address}', '{city}', '{region}', '{postal_code}', '{country}', 
                                      '{phone}')""").commit
        return self.new_add

    def get_create_admin(self):
        return self.new_add

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
                return """too many attempts. Closing program. Please contact another administrator. As an administrator 
                       with responsibility over passwords it does not look good that you forgot your password"""

    def get_by_id(self, table, col, val):
        return self.sql_query(str(f"SELECT * FROM {table} WHERE {col} = '{val}'")).fetchall()

    def get_all(self, table, col, name=None):
        result_list = []
        if name is None:
            query_result = self.sql_query(f"SELECT * FROM {table}")
        else:
            query_result = self.sql_query(f"SELECT * FROM {table} WHERE {col} LIKE '%{name}%'")
        while True:
            row = query_result.fetchone()
            if row is None:
                break
            result_list.append(row)
        return result_list

    def _create_table(self, col, data_type):
        self.new_table = self.sql_query(f"""CREATE TABLE table_name (
                                        {col} {data_type},
                                        {col} {data_type})""").commit
        return self.new_table

    def get_create_table(self):
        return self.new_table

    def _add_col(self, table, col, data_type):
        self.new_col = self.sql_query(f"ALTER TABLE {table} ADD {col} {data_type}").commit
        return self.new_col

    def get_drop(self):
        return self.new_col

    def _drop_table(self, table):
        self.new_drop = self.sql_query(f"DROP TABLE {table}").commit
        return self.new_drop

    def get_drop_table(self):
        return self.new_drop

    def _del_record(self, table, col, val):
        self.new_del_record = self.sql_query(f"DELETE FROM {table} WHERE {col}= '{val}'").commit
        return self.new_del_record

    def get_del_record(self):
        return self.new_del_record

    def _update_db(self, column_1, val_1, column_2, condition):
        self.update = self.sql_query(f"""UPDATE Products SET {column_1} = '{val_1}' WHERE {column_2} = 
                                     '{condition}'""").commit
        return self.update

    def get_update_db(self):
        return self.update

    def _insert_into(self, table, col, val):
        self.new_insert = self.sql_query(f"INSERT INTO {table} ({col}) VALUES ({val};").commit
        return self.new_insert

    def get_insert(self):
        return self.new_insert



