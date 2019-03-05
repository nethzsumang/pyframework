import tkinter as tk

from framework.GUI.tkinter.components.Component import Component
from framework.GUI.tkinter.components.Editable import Editable


class CheckButton(Component, Editable):
    def add(self, parent, options):
        self.set_data_type(Editable.INT)
        options["variable"] = self.var
        self.object = tk.Checkbutton(parent, options)
        return self
