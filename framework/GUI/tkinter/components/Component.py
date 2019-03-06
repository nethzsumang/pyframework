import abc


class Component(abc.ABC):
    @abc.abstractmethod
    def add(self, parent, options):
        pass

    def grid(self, row, col, columnspan=1):
        self.object.grid(row=row, column=col, columnspan=columnspan)
        return self

    def pack(self):
        self.object.pack()
        return self
