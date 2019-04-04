from framework.MVC.Model import Model


class Post(Model):
    def __init__(self):
        self.table = "posts"
        self.db_ref = True
        super().__init__()

