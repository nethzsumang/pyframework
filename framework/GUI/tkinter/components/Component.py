import abc


class Component(abc.ABC):
    @abc.abstractmethod
    def add(self, parent, options):
        pass

    def grid(self, row, col):
        self.object.grid(row=row, column=col)

    def pack(self):
        self.object.pack()
