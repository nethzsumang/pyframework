from framework.Data.Database.Database import Database
import abc


class Model(abc.ABC):
    def __init__(self):
        if self.db_ref:
            self.data_source = Database().init()
