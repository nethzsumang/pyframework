from abc import ABC, abstractmethod
from framework.Data.File.JSONFile import JSONFile
from framework.Utilities.Misc.Utils import path_join


class BaseClient:
    def __init__(self, options):
        self.options = options
    
    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def select(self, table, cols=[]):
        pass