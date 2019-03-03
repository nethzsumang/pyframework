import os
from framework.MVC.Controller import Controller


class IndexController(Controller):
    @staticmethod
    def index(o_app, a_params):
        print("This is " + o_app.get("APP", "APP_NAME") + " app.")
        from framework.Data.Database.Database import Database
        db = Database()
        db.init()
        o_app.dump(db.select('users', cols=['first_name', 'last_name']))
        return Controller.redirect(False)
