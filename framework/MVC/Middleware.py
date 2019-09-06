import abc


class Middleware(abc.ABC):
    def __init__(self):
        pass

    def execute(self):
        pass

    @abc.abstractmethod
    def handle(self, app, request):
        pass
    
    @staticmethod
    def next(request):
        return {
            "success": True,
            "request": request
        }
    
    @staticmethod
    def error(request, code=500, message="Error"):
        return {
            "success": False,
            "request": request,
            "code"   : code,
            "message": message
        }
