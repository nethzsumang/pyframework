from framework.Data.File.JSONFile import JSONFile
from framework.Utilities.Misc.Utils import path_join
from framework.Data.Database.Clients.Client import Client


class Database:
    def __init__(self):
        pass

    def init(self):
        """
            Initializes the database.
            :return:
        """
        a_options = JSONFile(path_join("config", "database.json"), "r").read()
        self.client = Client.connect(a_options)
        return self

    def select(self, table, cols=[]):
        """
            Gets the data from the table.
            :param table:
            :param cols:
            :return:
        """
        return self.client.select(table, cols)

    def raw_select(self, query):
        """
            Executes a raw query.
            :param query:
            :return:
        """
        return self.client.raw_select(query)

    def where(self, col, operation, value, connector="AND"):
        """
            Sets WHERE clauses for Select queries.
            :param col:
            :param operation:
            :param value:
            :param connector:
            :return:
        """
        self.client.where(col, operation, value, connector)
        return self

    def insert(self, table, data):
        """
            Inserts the data to the table.
            :param table:
            :param data:
            :return:
        """
        return self.client.insert(table, data)

    def update(self, table, data):
        """
            Updates one or more rows matched by WHERE clauses
            previously set with the data provided.
            :param table:
            :param data:
            :return:
        """
        return self.client.update(table, data)

    def delete(self, table):
        """
            Deletes one or more rows matched by WHERE clauses
            previously set.
            :param table:
            :return:
        """
        return self.client.delete(table)
