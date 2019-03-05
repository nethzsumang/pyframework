import tkinter as tk

from framework.GUI.tkinter.components.Component import Component


class Label(Component):
    def add(self, parent, options):
        self.object = tk.Label(parent, options)
        return self
