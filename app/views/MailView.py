from framework.MVC.View import View
from framework.GUI.tkinter.TkinterWrapper import TkinterWrapper

from app.views.events.MailEvents import MailEvents


class MailView(View):
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
                "command": lambda: MailEvents.handle(
                    "MailEvents.check_mail",
                    {
                        "sender": sender.get_value(),
                        "recipient": recipient.get_value(),
                        "message": message.get_string("1.0"),
                    },
                ),
            },
        ).grid(4, 0)

        TkinterWrapper.add_widget(
            frame,
            TkinterWrapper.BUTTON,
            {
                "text": "Send Email",
                "command": lambda: MailEvents.handle(
                    "MailEvents.send_mail",
                    {
                        "sender": sender.get_value(),
                        "recipient": recipient.get_value(),
                        "message": message.get_string("1.0"),
                    },
                ),
            },
        ).grid(4, 1)
