class BaseValidator:
    def __init__(self):
        pass

    def validate(self, m_var, s_rule, s_option):
        if (
            s_rule
            not in self.instance_rules
            + self.length_rules
            + self.content_rules
            + self.value_rules
        ):
            raise Exception("Invalid validator. Validator rule not found.")

        if s_rule in self.length_rules and (s_option is None or len(s_option) == 0):
            raise Exception("Invalid validator. Must have option to work.")

        if s_rule in self.value_rules and (s_option is None or len(str(s_option)) == 0):
            raise Exception("Invalid validator. Must have option to work.")

        if (s_rule in self.instance_rules or s_rule in self.content_rules) and (
            s_option is not None and len(s_option) > 0
        ):
            raise Exception("Invalid validator. This type does not accept values.")

        return getattr(self, s_rule)(m_var, s_option)
