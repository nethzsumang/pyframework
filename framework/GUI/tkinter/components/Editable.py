import tkinter as tk


class Editable:
    def set_data_type(self, dataType):
        if dataType == "string":
            self.var = tk.StringVar()
        elif dataType == "int":
            self.var = tk.IntVar()
        elif dataType == 'double':
            self.var = tk.DoubleVar()

    def get_value(self):
        return self.var.get()
    
    def set_value(self, data):
        self.var.set(data)

Editable.STRING = "string"
Editable.INT = "int"
Editable.DOUBLE = "double"