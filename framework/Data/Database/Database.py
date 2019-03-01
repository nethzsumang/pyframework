from framework.Data.File.JSONFile import JSONFile
from framework.Utilities.Misc.Utils import path_join
from framework.Data.Database.Clients.Client import Client


class Database:
    def __init__(self):
        pass
    
    def init(self):
        a_options = JSONFile(path_join('config', 'database.json'), 'r').read()
        self.client = Client.connect(a_options)

    def select(self, table, cols=[]):
        return self.client.select(table, cols)
