from framework.MVC.Controller import Controller
from framework.MVC.Response.Response import Response


class IndexController(Controller):
    @staticmethod
    def index(app):
        print("This is " + app.data["APP"]["APP_NAME"] + " app.")
        Controller.view('Sample', {})
        return Response.new(route="foo", data={})

    @staticmethod
    def foo(app):
        print("Foo method")
        return Response.new()
