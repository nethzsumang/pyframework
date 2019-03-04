from framework.Data.Database.Clients.BaseClient import BaseClient
import MySQLdb 

from urllib import parse


class MySQLClient(BaseClient):
    def connect(self):
        self.conn = MySQLdb.connect(
            host=self.options["options"]["host"],
            port=self.options["options"]["port"],
            user=self.options["options"]["user"],
            passwd=self.options["options"]["password"],
            db=self.options["options"]["database"],
        )
        self.where_str = ""
        self.cursor = self.conn.cursor(MySQLdb.cursors.DictCursor)
    
    def select(self, table, cols=[]):
        col_names = ''
        if len(cols) > 0:
            cols = map(lambda colname: parse.quote(colname), cols)
            col_names = ','.join(cols)
        else:
            col_names = '*'

        table = parse.quote(table)

        if len(self.where_str) > 0:
            self.where_str = 'WHERE ' + self.where_str

        query_str = 'SELECT ' + col_names + ' FROM ' + table + ' ' + self.where_str

        self.cursor.execute(query_str)
        self.where_str = ""
        return self.cursor.fetchall()

    def raw_select(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def where(self, col, operation, value, connector):
        if len(self.where_str) > 0:
            self.where_str = self.where_str + ' ' + connector + ' ' + col + operation + "'" + str(value) + "'"
        else:
            self.where_str = self.where_str + col + operation + "'" + str(value) + "'"
        return self
    
    def insert(self, table, data):
        table = parse.quote(table)
        query_str = "INSERT INTO " + table + " "
        column_str = "("
        value_str = "("
        index = 0

        for col, val in data.items():
            if index == 0:
                column_str = column_str + col
                value_str = value_str + r"%s"
            else:
                column_str = column_str + "," + col
                value_str = value_str + "," + r"%s"
            
            index = index + 1
        
        column_str = column_str + ")"
        value_str = value_str + ")"

        query_str = query_str + column_str + " VALUES " + value_str
        return_val = self.cursor.execute(query_str, tuple(data.values()))
        self.conn.commit()   
        return return_val
    
    def update(self, table, data):
        table = parse.quote(table)
        query_str = "UPDATE " + table + " SET "
        data_str = ""
        index = 0

        for col, val in data.items():
            if index == 0:
                data_str = col + r"=%s"
            else:
                data_str = "," + col + r"=%s"
        
        query_str = query_str + data_str + " WHERE " + self.where_str
        return_val = self.cursor.execute(query_str, tuple(data.values()))
        self.conn.commit()
        return return_val

