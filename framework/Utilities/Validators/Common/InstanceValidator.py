class InstanceValidator:
    def __init__(self):
        pass

    def required(self, m_var):
        if m_var is None:
            return False

        if self.has_len(m_var):
            if len(m_var) == 0:
                return False

        return True

    def optional(self, m_var):
        return True

    def has_len(self, m_var):
        if isinstance(m_var, str) or isinstance(m_var, list) or isinstance(m_var, dict):
            return True
        return False
