class NumericValidator:
    def __init__(self):
        pass

    def minval(self, m_value, min):
        if m_value < min:
            return False
        return True

    def maxval(self, m_value, max):
        if m_value > max:
            return False
        return True
