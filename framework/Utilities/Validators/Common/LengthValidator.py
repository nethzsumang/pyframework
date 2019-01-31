class LengthValidator:
    def __init__(self):
        pass

    def max(self, m_var, s_option):
        if len(m_var) > int(s_option):
            return self.error_msg['max'] % str(s_option)
        return True

    def min(self, m_var, s_option):
        if len(m_var) < int(s_option):
            return self.error_msg['min'] % str(s_option)
        return True
