from framework.Data.File.JSONFile import JSONFile
from framework.Utilities.Misc.Utils import path_join
from framework.Data.Database.Clients.Client import Client


class Database:
    def __init__(self):
        pass
    
    def init(self):
        a_options = JSONFile(path_join('config', 'database.json'), 'r').read()
        self.client = Client.connect(a_options)
        return self

    def select(self, table, cols=[]):
        return self.client.select(table, cols)

    def raw_select(self, query):
        return self.client.raw_select(query)

    def where(self, col, operation, value, connector='AND'):
        self.client.where(col, operation, value, connector)
        return self
    
    def insert(self, table, data):
        return self.client.insert(table, data)
    
    def update(self, table, data):
        return self.client.update(table, data)
