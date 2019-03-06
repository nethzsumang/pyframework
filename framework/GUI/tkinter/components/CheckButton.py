import tkinter as tk

from framework.GUI.tkinter.components.Component import Component
from framework.GUI.tkinter.components.interfaces.Editable import Editable
from framework.GUI.tkinter.components.interfaces.Selectable import Selectable


class CheckButton(Component, Editable, Selectable):
    def add(self, parent, options):
        self.set_data_type(Editable.INT)
        options["variable"] = self.var
        self.object = tk.Checkbutton(parent, options)
        return self
