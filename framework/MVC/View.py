import abc


class View(abc.ABC):
    def __init__(self):
        pass

    @abc.abstractmethod
    def show(self, a_data):
        pass

    @abc.abstractmethod
    def close(self):
        pass
