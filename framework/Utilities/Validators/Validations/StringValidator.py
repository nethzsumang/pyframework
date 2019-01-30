from framework.Utilities.Validators.Common.BaseValidator import BaseValidator
from framework.Utilities.Validators.Common.LengthValidator import LengthValidator
from framework.Utilities.Validators.Common.InstanceValidator import InstanceValidator


class StringValidator(BaseValidator, LengthValidator, InstanceValidator):
    instance_rules = ['required', 'optional']
    length_rules = ['max', 'min']
    content_rules = ['alpha', 'alphanumeric']
    value_rules = []

    error_msg = {
        'max': 'Variable\'s length must be greater than or equal to %s.',
        'min': 'Variable\'s length must be less than or equal to %s.',
        'required': 'Variable is required.',
        'optional': 'Variable is not required?'
    }
