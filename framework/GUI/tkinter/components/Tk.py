import tkinter as tk

from framework.GUI.tkinter.components.Component import Component


class Tk(Component):
    def add(self, parent, options):
        self.object = tk.Tk()
        return self
