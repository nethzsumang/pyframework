from framework.Utilities.Validators.Validations import StringValidator, NumericValidator

class Validator:
	options = {}

	'''
		a_data = {'x': 'hiii', 'y': 4}
		a_rules = {'x': 'required|max:5', 'y': 'optional|maxval:3'}
	'''
	def validate(self, a_data, a_rules, a_options=None):
		for data_key, data_value in a_data.items():
			if isinstance(data_value, int):
				self.exec_validation('int', data_value, a_rules[data_key].split('|'))
			elif isinstance(data_value, str):
				pass

	def exec_validation(self, s_data_type, m_data, a_validations):
		o_numeric_validator = NumericValidator()
		o_string_validator = StringValidator()
