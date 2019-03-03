from framework.Data.Database.Database import Database
import abc


class Model(abc.ABC):
    def __init__(self):
        if self.db_ref:
            self.data_source = Database().init()

    def select(self, cols=[]):
        return self.data_source.select(self.table, cols)

    def raw_select(self, query):
        return self.data_source.raw_select(query)

    def where(self, col, operation, value):
        self.data_source.where(col, operation, value)
        return self
