import unittest
import string
from string import Template
import test_string

def test_idpattern_override_inside_outside():

    class MyPattern(Template):
        idpattern = '[a-z]+'
        braceidpattern = '[A-Z]+'
        flags = 0
    m = dict(foo='foo', BAR='BAR')
    s = MyPattern('$foo ${BAR}')
    TestTemplate.assertEqual(s.substitute(m), 'foo BAR')

TestTemplate = test_string.TestTemplate()
test_idpattern_override_inside_outside()
