from framework.MVC.Middleware import Middleware


class SampleMiddleware(Middleware):
    def __init__(self):
        super().__init__()

    def handle(self, request):
        pass
