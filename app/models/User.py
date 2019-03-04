from framework.MVC.Model import Model


class User(Model):
    def __init__(self):
        self.table = 'users'
        self.db_ref = True
        super().__init__()
