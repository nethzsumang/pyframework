from abc import ABC


class Component(ABC):
    @abstractmethod
    def add(self, parent, options):
        pass