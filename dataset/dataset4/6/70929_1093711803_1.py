py_warnings = support.import_fresh_module('warnings', blocked=['_warnings'])
c_warnings = support.import_fresh_module('warnings', fresh=['_warnings'])