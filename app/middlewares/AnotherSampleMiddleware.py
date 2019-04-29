from framework.MVC.Middleware import Middleware
from framework.MVC.Request.Request import Request


class AnotherSampleMiddleware(Middleware):
    def __init__(self):
        super().__init__()

    def handle(self, app, request):
        request.set_data('name', 'Edited')
        if not request.get_data('flag'):
            return Request.create(app, 'error')

        print('another sample middleware')
        return
