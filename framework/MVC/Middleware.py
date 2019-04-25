import abc


class Middleware(abc.ABC):
    def __init__(self):
        pass

    def execute(self):
        pass

    @abc.abstractmethod
    def handle(self, request):
        pass