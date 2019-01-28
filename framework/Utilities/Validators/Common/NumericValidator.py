class NumericValidator:
    error_msg = {
        'minval': 'Variable\'s value must be greater than or equal to %s.',
        'maxval': 'Variable\'s value must be less than or equal to %s.'
    }

    def __init__(self):
        pass

    def minval(self, m_value, min):
        from var_dump import var_dump
        var_dump(self.error_msg)
        if m_value < float(min):
            return self.error_msg['minval'] % str(min)
        return True

    def maxval(self, m_value, max):
        if m_value > float(max):
            return self.error_msg['maxval'] % str(max)
        return True
