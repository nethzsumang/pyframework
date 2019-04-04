from framework.Data.Database.Clients.BaseClient import BaseClient
import MySQLdb

from urllib import parse


class MySQLClient(BaseClient):
    def connect(self):
        """
            Connects to the database.
            :return:
        """
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
        """
            Gets the data from the table.
            :param table:
            :param cols:
            :return:
        """
        col_names = ""
        if len(cols) > 0:
            cols = map(lambda colname: parse.quote(colname), cols)
            col_names = ",".join(cols)
        else:
            col_names = "*"

        table = parse.quote(table)

        if len(self.where_str) > 0:
            self.where_str = "WHERE " + self.where_str

        query_str = "SELECT " + col_names + " FROM " + table + " " + self.where_str

        self.cursor.execute(query_str)
        self.where_str = ""
        return self.cursor.fetchall()

    def raw_select(self, query):
        """
            Executes a raw query.
            :param query:
            :return:
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def where(self, col, operation, value, connector):
        """
            Sets WHERE clauses for Select queries.
            :param col:
            :param operation:
            :param value:
            :param connector:
            :return:
        """
        if len(self.where_str) > 0:
            self.where_str = (
                self.where_str
                + " "
                + connector
                + " "
                + col
                + operation
                + "'"
                + str(value)
                + "'"
            )
        else:
            self.where_str = self.where_str + col + operation + "'" + str(value) + "'"
        return self

    def insert(self, table, data):
        """
            Inserts the data to the table.
            :param table:
            :param data:
            :return:
        """
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
        """
            Updates one or more rows matched by WHERE clauses
            previously set with the data provided.
            :param table:
            :param data:
            :return:
        """
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

    def delete(self, table):
        """
            Deletes one or more rows matched by WHERE clauses
            previously set.
            :param table:
            :return:
        """
        table = parse.quote(table)
        query_str = "DELETE FROM " + table + " WHERE " + self.where_str
        return_val = self.cursor.execute(query_str)
        self.conn.commit()
        return return_val

    def migrate(self, schema):
        from framework.Utilities.Misc.Dict import Dict
        import os

        table = Dict.get(schema, 'table')
        keys = Dict.get(schema, 'keys')
        fields = Dict.get(schema, 'fields')

        query = 'CREATE TABLE ' + table + ' (\n'

        for field in fields:
            name = Dict.get(field, 'name')
            type = Dict.get(field, 'type')
            length = Dict.get(field, 'length')
            nullable = Dict.get(field, 'nullable', False)
            default = Dict.get(field, 'default', None)
            auto_increment = Dict.get(field, 'autoIncrement', False)

            query = query + name + ' ' + type

            if length is not None:
                query = query + '(' + str(length) + ')'

            query = query + ' '

            if not nullable:
                query = query + 'NOT NULL '

            if default is not None:
                query = query + 'DEFAULT \'' + default + '\' '

            if auto_increment:
                query = query + ' AUTO_INCREMENT'

            query = query + ","

        primary_key = Dict.get(keys, 'primaryKey', None)
        foreign_keys = Dict.get(keys, 'foreignKeys')

        if primary_key is not None:
            query = query + 'PRIMARY KEY (' + primary_key + '),'

        if foreign_keys is not None:
            for foreign in foreign_keys:
                column_name = Dict.get(foreign, 'columnName')
                references = Dict.get(foreign, 'references')
                on = Dict.get(foreign, 'on')

                query = query + 'FOREIGN KEY (' + column_name + ') REFERENCES ' + on + '(' + references + '),'

        query = query[:-1] + ');'

        return self.cursor.execute(query)




