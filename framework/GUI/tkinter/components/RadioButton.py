import tkinter as tk

from framework.GUI.tkinter.components.Component import Component
from framework.GUI.tkinter.components.interfaces.Editable import Editable
from framework.GUI.tkinter.components.interfaces.Selectable import Selectable


class RadioButton(Component, Editable, Selectable):
    def add(self, parent, options):
        if "groupElement" not in options or options["groupElement"] is None:
            dataType = options.pop("dataType", Editable.STRING)
            self.set_data_type(dataType)
            options["variable"] = self.var
        else:
            options["variable"] = options.pop("groupElement").var
            self.var = options["variable"]
        self.object = tk.Radiobutton(parent, options)
        return self
