import abc


class View(abc.ABC):
    def __init__(self, data):
        self.data = data;

    @abc.abstractmethod
    def show(self):
        pass

    @abc.abstractmethod
    def close(self):
        pass
