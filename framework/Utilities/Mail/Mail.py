import smtplib


class Mail:
    def __init__(self):
        from framework.Data.File.JSONFile import JSONFile
        import os
        from pathlib import Path

        lang_data_path = str(Path.cwd()) + os.sep + "config" + os.sep + "mail.json"
        self.options = JSONFile(lang_data_path, "r").read()

    def send(self, message, to, sender=None):
        sender = sender if sender is not None else self.options["default_sender"]

        try:
            o_smtp = smtplib.SMTP(self.options["host"])
            o_smtp.sendmail(sender, to, message)
            return True
        except smtplib.SMTPException:
            return False

    @staticmethod
    def is_valid_email(email):
        import re

        if len(email) > 7:
            return bool(
                re.match(
                    "^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email
                )
            )
        return False
