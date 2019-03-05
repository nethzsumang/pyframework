import tkinter as tk

from framework.GUI.tkinter.components.Component import Component


class Button(Component):
    def add(self, parent, options):
        self.object = tk.Button(
            parent, text=options["text"], command=options["command"]
        )
        return self
