import smtplib


class Mail:
    def __init__(self, options):
        self.options = {
            "host": options["host"],
            "port": options["port"],
            "default_sender": options["sender"],
        }

    def send(self, message, to, sender=None):
        sender = sender if sender is not None else self.options["default_sender"]

        try:
            o_smtp = smtplib.SMTP(self.options["host"])
            o_smtp.sendmail(sender, to, message)
            return True
        except smtplib.SMTPException:
            return False
