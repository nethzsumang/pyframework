from framework.Data.File.JSONFile import JSONFile
from framework.Utilities.Misc.Utils import path_join


class Database:
    def __init__(self):
        pass
    
    @staticmethod
    def init():
        a_options = JSONFile(path_join('config', 'database.json'), 'r').read()
