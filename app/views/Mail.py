from framework.MVC.View import View
from framework.GUI.tkinter.TkinterWrapper import TkinterWrapper
from framework.Utilities.Mail.Mail import Mail


class Mail(View):
    def __init__(self):
        super().__init__()
        self._initElements()
    
    def show(self, a_data):
        TkinterWrapper.open_window(self.root)
    
    def close(self):
        TkinterWrapper.close_window(self.root)

    def _initElements(self):
        self.root = TkinterWrapper.create_instance()
        frame = TkinterWrapper.add_widget(self.root, TkinterWrapper.FRAME, {}).pack()

        TkinterWrapper.add_widget(
            frame,
            TkinterWrapper.LABEL,
            {"text": "Enter your email:", "justify": "left"},
        ).grid(0, 0)
        sender = TkinterWrapper.add_widget(
            frame, TkinterWrapper.ENTRY, {"width": 30, "dataType": "string"}
        ).grid(0, 1)

        TkinterWrapper.add_widget(
            frame,
            TkinterWrapper.LABEL,
            {"text": "Enter your recipient's email:", "justify": "left"},
        ).grid(1, 0)
        recipient = TkinterWrapper.add_widget(
            frame, TkinterWrapper.ENTRY, {"width": 30, "dataType": "string"}
        ).grid(1, 1)

        TkinterWrapper.add_widget(
            frame, TkinterWrapper.LABEL, {"text": "Enter your message"}
        ).grid(2, 0)
        message = TkinterWrapper.add_widget(
            frame, TkinterWrapper.TEXT, {"height": 20, "width": 50}
        ).grid(3, 0, 2)

        TkinterWrapper.add_widget(
            frame,
            TkinterWrapper.BUTTON,
            {
                "text": "Check Email",
                "command": lambda: print("Emails are valid!")
                if Mail.is_valid_email(sender.get_value())
                and Mail.is_valid_email(recipient.get_value())
                else print("There is/are invalid emails!"),
            },
        ).grid(4, 0)

        TkinterWrapper.add_widget(
            frame,
            TkinterWrapper.BUTTON,
            {
                "text": "Send Email",
                "command": lambda: Mail().send(
                    message.get_string("1.0"), recipient.get_value(), sender.get_value()
                ),
            },
        ).grid(4, 1)
