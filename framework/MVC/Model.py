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

    def where(self, col, operation, value, connector="AND"):
        self.data_source.where(col, operation, value, connector=connector)
        return self

    def insert(self, data):
        return self.data_source.insert(self.table, data)

    def update(self, data):
        return self.data_source.update(self.table, data)

    def delete(self):
        return self.data_source.delete(self.table)

    def migrate(self):
        return self.data_source.migrate(self.table)
