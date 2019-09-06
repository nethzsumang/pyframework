from framework.MVC.Middleware import Middleware
from framework.MVC.Response.Response import Response


class SampleMiddleware(Middleware):
    def __init__(self):
        super().__init__()

    def handle(self, app, request):
        request.set_data('name', 'Kenneth')
        request.set_data('flag', True)
        print('sample middleware')
        return Middleware.next(request)
