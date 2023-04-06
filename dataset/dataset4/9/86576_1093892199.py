
import functools
from test.support import import_helper

partial = functools.partial
new_functools = import_helper.import_fresh_module('functools',
                                                  fresh=['_functools'])
new_partial = new_functools.partial
assert(partial == new_partial)
