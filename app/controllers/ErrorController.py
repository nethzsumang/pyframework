from framework.MVC.Controller import Controller
import sys


class ErrorController(Controller):
    @staticmethod
    def error500(app):
        print("Error 500")
        sys.exit(500)
