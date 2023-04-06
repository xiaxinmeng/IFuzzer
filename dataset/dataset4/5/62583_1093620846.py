import warnings
from test import support

saved = warnings.filters.copy()

c_warnings = support.import_fresh_module('warnings', fresh=['_warnings'])