class LengthValidator:
    error_msg = {
        'max': 'Variable\'s length must be greater than or equal to %s.',
        'min': 'Variable\'s length must be less than or equal to %s.'
    }

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
