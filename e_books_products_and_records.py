from e_books_connect import MSDBConnection

nwind = MSDBConnection()


class DbBookTable(MSDBConnection):


    def create_entry(self, productName, supplierID, categoryID, quantityPerUnit,
                               unitsInStock, unitsOnOrder, reorderLevel, discontinued):
        return self.sql_query(f"""INSERT INTO Products (ProductName, SupplierID, CategoryID, QuantityPerUnit,
                               UnitsInStock, UnitsOnOrder, ReorderLevel, Discontinued)
                               VALUES ('{productName}', {supplierID}, {categoryID}, '{quantityPerUnit}', 
                                {unitsInStock}, {unitsOnOrder}, {reorderLevel}, {discontinued})""").commit

    def get_by_id(self, id):
        return self.sql_query(f"SELECT * FROM Products WHERE ProductID = " + str(id)).fetchone()

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



class CRUDRecord(DbBookTable):

    new_record = DbBookTable().get_by_id(id)

    def create_record(self, new_record):
        return self.sql_query(f"SELECT * FROM Products WHERE ProductName LIKE '%{''}.%'").new_record()
