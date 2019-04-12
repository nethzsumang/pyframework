from framework.MVC.Controller import Controller


class IndexController(Controller):
    @staticmethod
    def index(app, params):
        print("This is " + app.data["APP"]["APP_NAME"] + " app.")
        Controller.view('Sample', {})
        return Controller.redirect(False)
