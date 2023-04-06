python/cpython#36890
import re
list(re.finditer('\s', 'a b'))
# expected: one item list
# bug: hang

#Kevin J. Butler
import re
list(re.finditer('.*', 'asdf'))
# expected: two item list (?)
# bug: hang