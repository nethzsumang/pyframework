class ContentValidator:
    def __init__(self):
        pass

    def alpha(self, m_var, m_option):
        import re

        return (
            True
            if re.match("^[a-zA-Z]+$", m_var, re.X) is not None
            else self.error_msg["alpha"]
        )

    def alphanumeric(self, m_var, m_option):
        import re

        return (
            True
            if re.match("^[a-zA-Z0-9]+$", m_var, re.X) is not None
            else self.error_msg["alphanumeric"]
        )
