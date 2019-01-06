from framework.MVC.Controller import Controller
import sys


class ErrorController(Controller):
    @staticmethod
    def index(o_app, a_params):
        print('Error ' + str(a_params['code']))
        print(a_params['msg'])
        sys.exit(a_params['code'])
