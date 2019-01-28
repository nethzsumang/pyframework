class InstanceValidator:
    error_msg = {
        'required': 'Variable is required.',
        'optional': 'Variable is not required?'
    }

    def __init__(self):
        pass

    def required(self, m_var, s_option):
        if m_var is None:
            return self.error_msg['required']

        if self.has_len(m_var):
            if len(m_var) == 0:
                return self.error_msg['required']

        return True

    def optional(self, m_var, s_option):
        return True

    def has_len(self, m_var):
        if isinstance(m_var, str) or isinstance(m_var, list) or isinstance(m_var, dict):
            return True
        return False
