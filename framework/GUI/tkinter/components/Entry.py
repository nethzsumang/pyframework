import tkinter as tk

from framework.GUI.tkinter.components.Component import Component
from framework.GUI.tkinter.components.Editable import Editable


class Entry(Component, Editable):
    def add(self, parent, options):
        dataType = options.pop("dataType", Editable.STRING)
        self.set_data_type(dataType)
        options["textvariable"] = self.var
        self.object = tk.Entry(parent, options)
        return self
