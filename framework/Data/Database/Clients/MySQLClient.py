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
        self.cursor = self.conn.cursor()
    
    def select(self, table, cols=[]):
        col_names = ''
        if len(cols) > 0:
            cols = map(lambda colname: parse.quote(colname), cols)
            col_names = ','.join(cols)
        else:
            col_names = '*'
        
        table = parse.quote(table)
        self.cursor.execute('SELECT ' + col_names + ' FROM ' + table)
        return self.cursor.fetchall()
