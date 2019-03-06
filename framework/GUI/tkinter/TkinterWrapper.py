import tkinter as tk


class TkinterWrapper:
    @staticmethod
    def create_instance():
        from framework.GUI.tkinter.components.Tk import Tk

        return Tk().add(None, {})

    @staticmethod
    def add_widget(parent, eltype, options={}):
        from pydoc import locate

        o_class = locate("framework.GUI.tkinter.components." + eltype + "." + eltype)
        return getattr(o_class, "add")(o_class(), parent.object, options)

    @staticmethod
    def open_window(element):
        element.object.mainloop()

    @staticmethod
    def close_window(element):
        element.object.destroy()


TkinterWrapper.FRAME = "Frame"
TkinterWrapper.BUTTON = "Button"
TkinterWrapper.LABEL = "Label"
TkinterWrapper.ENTRY = "Entry"
TkinterWrapper.CHECKBUTTON = "CheckButton"
TkinterWrapper.RADIOBUTTON = "RadioButton"
TkinterWrapper.TEXT = "Text"
