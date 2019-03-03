from framework.Utilities.Validators.Common.BaseValidator import BaseValidator
from framework.Utilities.Validators.Common.InstanceValidator import InstanceValidator
from framework.Utilities.Validators.Common.NumericValidator import NumericValidator


class NumericValidator(BaseValidator, InstanceValidator, NumericValidator):
    instance_rules = ["required", "optional"]
    length_rules = []
    content_rules = []
    value_rules = ["maxval", "minval"]

    error_msg = {
        "minval": "Variable's value must be greater than or equal to %s.",
        "maxval": "Variable's value must be less than or equal to %s.",
        "required": "Variable is required.",
        "optional": "Variable is not required?",
    }
