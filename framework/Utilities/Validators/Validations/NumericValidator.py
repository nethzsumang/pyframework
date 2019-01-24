from framework.Utilities.Validators.Common.BaseValidator import BaseValidator
from framework.Utilities.Validators.Common.InstanceValidator import InstanceValidator
from framework.Utilities.Validators.Common.NumericValidator import NumericValidator


class NumericValidator(BaseValidator, InstanceValidator, NumericValidator):
    instance_rules = ['required', 'optional']
    length_rules = []
    content_rules = []
    value_rules = ['maxval', 'minval']