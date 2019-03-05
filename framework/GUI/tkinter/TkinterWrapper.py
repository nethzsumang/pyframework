import tkinter as tk

from framework.GUI.tkinter.components import *


class TkinterWrapper:
    @staticmethod
    def create_instance():
        return tk.Tk()
    
    @staticmethod
    def add_widget(parent, eltype, options={}):
        from pydoc import locate

        o_class = locate("framework.GUI.tkinter.components." + eltype)
        return getattr(o_class, "add")(parent, options)


TkinterWrapper.FRAME = "Frame"
TkinterWrapper.BUTTON = "Button"
TkinterWrapper.LABEL = "Label"