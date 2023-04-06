import unittest
import string
from string import Template
import test_string

def test_SafeTemplate():
    eq = TestTemplate.assertEqual
    s = Template('$who likes ${what} for ${meal}')
    eq(s.safe_substitute(dict(who='tim')), 'tim likes ${what} for ${meal}')
    eq(s.safe_substitute(dict(what='ham')), '$who likes ham for ${meal}')
    eq(s.safe_substitute(dict(what='ham', meal='dinner')), '$who likes ham for dinner')
    eq(s.safe_substitute(dict(who='tim', what='ham')), 'tim likes ham for ${meal}')
    eq(s.safe_substitute(dict(who='tim', what='ham', meal='dinner')), 'tim likes ham for dinner')

TestTemplate = test_string.TestTemplate()
test_SafeTemplate()
