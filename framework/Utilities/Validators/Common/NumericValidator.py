class NumericValidator:
    def __init__(self):
        pass

    def minval(self, m_value, min):
        if m_value < float(min):
            return self.error_msg['minval'] % str(min)
        return True

    def maxval(self, m_value, max):
        if m_value > float(max):
            return self.error_msg['maxval'] % str(max)
        return True
