from framework.Utilities.Validators.Validator import Validator


class StringValidator(Validator):
	def __init__(self):
		pass

	@staticmethod
	def validate(m_var):
		if not isinstance(m_var, str):
			return False

		return True

	@staticmethod
	def has_valid_length(m_var, i_min, i_max):
		if not StringValidator.validate(m_var):
			return False

		if len(m_var) < i_min or len(m_var) > i_max:
			return False

		return True
