import pyodbc


class MSDBConnection:

# should establish connection with any DB with have in MS_SQL
    def __init__(self, database='Northwind'):
        self.server = 'databases2.spartaglobal.academy'
        self.database = database
        self.username = 'SA'
        self.password = 'Passw0rd2018'
        self.con = self._establish_connection()
        self.cursor = self.con.cursor()

    def _establish_connection(self):
        connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.server+';'
                                    'DATABASE='+self.database+';''UID='+self.username+';PWD='+self.password)
        return connection

    def sql_query(self, sql_string):

        return self.cursor.execute(sql_string)