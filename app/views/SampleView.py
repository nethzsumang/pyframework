from framework.MVC.View import View
from framework.GUI.tkinter.TkinterWrapper import TkinterWrapper


class SampleView(View):
    def __init__(self, data):
        super().__init__(data)
        self._initElements()

    def show(self):
        TkinterWrapper.open_window(self.root)

    def close(self):
        TkinterWrapper.close_window(self.root)

    def _initElements(self):
        self.root = TkinterWrapper.create_instance()
        frame = TkinterWrapper.add_widget(self.root, TkinterWrapper.FRAME, {}).pack()

        TkinterWrapper.add_widget(
            frame,
            TkinterWrapper.LABEL,
            {
                "text": "Hello, " + self.data["name"] + "!", 
                "justify": "center"
            }
        ).grid(0, 0)
