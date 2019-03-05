from framework.MVC.Controller import Controller


class IndexController(Controller):
    @staticmethod
    def index(o_app, a_params):
        print("This is " + o_app.get("APP", "APP_NAME") + " app.")
        from framework.GUI.tkinter.TkinterWrapper import TkinterWrapper

        root = TkinterWrapper.create_instance()
        frame = TkinterWrapper.add_widget(root, TkinterWrapper.FRAME, {}).pack()
        TkinterWrapper.add_widget(
            frame, TkinterWrapper.LABEL, {"text": "Enter your name"}
        ).pack()
        textbox = TkinterWrapper.add_widget(
            frame, TkinterWrapper.ENTRY, {"width": 10, "dataType": "string"}
        ).pack()
        checkbox = TkinterWrapper.add_widget(
            frame, TkinterWrapper.CHECKBUTTON, {"text": "Are you sure?"}
        ).pack()
        TkinterWrapper.add_widget(
            frame,
            TkinterWrapper.BUTTON,
            {
                "text": "Press Me!",
                "command": lambda: print("Hi, " + str(textbox.get_value()) + "!")
                if checkbox.get_value()
                else None,
            },
        ).pack()
        TkinterWrapper.add_widget(
            frame,
            TkinterWrapper.BUTTON,
            {
                "text": "Close Window",
                "command": lambda: TkinterWrapper.close_window(root),
            },
        ).pack()
        TkinterWrapper.open_window(root)
        return Controller.redirect(False)
