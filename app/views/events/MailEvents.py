from framework.MVC.Event import Event
from framework.Utilities.Mail.Mail import Mail
from framework.Utilities.Validators.Validator import Validator


class MailEvents(Event):
    @staticmethod
    def _check_mail(data):
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

        from var_dump import var_dump

        var_dump(result)

        if Mail.is_valid_email(sender) or Mail.is_valid_email(recipient):
            print("There is an invalid email.")
