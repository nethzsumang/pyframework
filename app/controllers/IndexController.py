from framework.MVC.Controller import Controller
from framework.MVC.Response.Response import Response


class IndexController(Controller):
    @staticmethod
    def index(app):
        print("This is " + app.data["APP"]["APP_NAME"] + " app.")
        print("From middleware: " + app.request.get_data('name'))
        Controller.view('Sample', {
            "name": app.request.get_data("name")
        })
        return Response.new(route="foo", data={})

    @staticmethod
    def foo(app):
        print("Foo method")
        return Response.exit()
