from bootstrap import bootstrap
from framework.Utilities.Packager import *
from framework.Utilities.Validators.Validations import StringValidator, NumericValidator
from var_dump import var_dump
obj = StringValidator.StringValidator()
obj2 = NumericValidator.NumericValidator()
var_dump(obj.validate('adsada', 'min', '6'))
var_dump(obj2.validate(45, 'minval', 44))

# version_check()
# o_app = bootstrap.start()
