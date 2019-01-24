from framework.Utilities.Validators.Common.BaseValidator import BaseValidator
from framework.Utilities.Validators.Common.LengthValidator import LengthValidator
from framework.Utilities.Validators.Common.InstanceValidator import InstanceValidator


class StringValidator(BaseValidator, LengthValidator, InstanceValidator):
	instance_rules = ['required', 'optional']
	length_rules = ['max', 'min']
	content_rules = ['alpha', 'alphanumeric']
	value_rules = []
