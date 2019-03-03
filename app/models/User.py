from framework.MVC.Model import Model


class User(Model):
    def __init__(self):
        super.__init__()
        self.table = 'users'
        self.db_ref = True