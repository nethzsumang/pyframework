from framework.Utilities.Validators.Validations import StringValidator, NumericValidator

class Validator:
	options = {}

	'''
		a_data = {'x': 'hiii', 'y': 4}
		a_rules = {'x': 'required|max:5', 'y': 'optional|maxval:3'}
	'''
	def validate(self, a_data, a_rules, a_options=None):
		a_validation_result = {}
		for data_key, data_value in a_data.items():
			s_rule = a_rules[data_key].split('|')
			if isinstance(data_value, int):
				a_result = self.exec_validation('int', data_value, s_rule)
			elif isinstance(data_value, str):
				a_result = self.exec_validation('str', data_value, s_rule)

			a_validation_result[data_key] = a_result

		return a_validation_result

	def exec_validation(self, s_data_type, m_data, a_validations):
		o_validator = None
		a_result = {}

		if s_data_type == 'int':
			o_validator = NumericValidator.NumericValidator()
		elif s_data_type == 'str':
			o_validator = StringValidator.StringValidator()

		for s_validation in a_validations:
			a_options = s_validation.split(':')

			if len(a_options) == 1:
				a_result[a_options[0]] = o_validator.validate(m_data, a_options[0], None)
			else:
				a_result[a_options[0]] = o_validator.validate(m_data, a_options[0], a_options[1])

		return a_result
