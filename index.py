from bootstrap import bootstrap
from framework.Utilities.Packager import *
from framework.Utilities.Validators.Validator import Validator
from var_dump import var_dump
obj = Validator()
res = obj.validate({'x': 1, 'y': 'apple'}, {'x': 'required|minval:2', 'y': 'required|min:6'})
var_dump(res)
# version_check()
# o_app = bootstrap.start()
