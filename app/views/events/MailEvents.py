from framework.MVC.Event import Event
from framework.Utilities.Mail.Mail import Mail
from framework.Utilities.Validators.Validator import Validator


class MailEvents(Event):
    @staticmethod
    def check_mail(data):
        message = data["message"]
        sender = data["sender"]
        recipient = data["recipient"]

        validator = Validator()
        result = validator.validate(
            {"sender": sender, "recipient": recipient, "message": message},
            {
                "sender": "required|min:7",
                "recipient": "required|min:7",
                "message": "required",
            },
        )

        from tkinter import messagebox

        if len(result.keys()) > 0:
            messagebox.showinfo("Validation Result", validator.get_errors())
        else:
            messagebox.showinfo("Validation Result", "All are valid!")

    @staticmethod
    def send_mail(data):
        message = data["message"]
        sender = data["sender"]
        recipient = data["recipient"]
