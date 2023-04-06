
from test.support.import_helper import import_fresh_module

copy_py = import_fresh_module('copy', blocked=['_copy'])
try:
    copy_c = import_fresh_module('copy', fresh=['_copy'])
except ImportError:
    copy_c = None
