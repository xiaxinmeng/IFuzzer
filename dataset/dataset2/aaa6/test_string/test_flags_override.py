import unittest
import string
from string import Template
import test_string

def test_flags_override():

    class MyPattern(Template):
        flags = 0
    s = MyPattern('$wHO likes ${WHAT} for ${meal}')
    d = dict(wHO='tim', WHAT='ham', meal='dinner', w='fred')
    TestTemplate.assertRaises(ValueError, s.substitute, d)
    TestTemplate.assertEqual(s.safe_substitute(d), 'fredHO likes ${WHAT} for dinner')

TestTemplate = test_string.TestTemplate()
test_flags_override()
