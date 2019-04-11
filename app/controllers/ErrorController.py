from framework.MVC.Controller import Controller
import sys


class ErrorController(Controller):
    @staticmethod
    def index(app, params):
        print("Error " + str(params["code"]))
        print(params["msg"])
        sys.exit(params["code"])
