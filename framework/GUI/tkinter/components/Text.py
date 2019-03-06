import tkinter as tk

from framework.GUI.tkinter.components.Component import Component
from framework.GUI.tkinter.components.interfaces.Editable import Editable


class Text(Component):
    def add(self, parent, options):
        self.object = tk.Text(parent, options)
        return self

    def get_string(self, startindex, endindex=None):
        return self.object.get(startindex, endindex)

    def set_string(self, string, index):
        self.object.insert(index, string)

    def delete_string(self, startindex, endindex=None):
        self.object.delete(startindex, endindex)
