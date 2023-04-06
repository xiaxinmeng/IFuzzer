import unittest
import string
from string import Template
import test_string

def test_regular_templates_with_braces():
    s = Template('$who likes ${what} for ${meal}')
    d = dict(who='tim', what='ham', meal='dinner')
    TestTemplate.assertEqual(s.substitute(d), 'tim likes ham for dinner')
    TestTemplate.assertRaises(KeyError, s.substitute, dict(who='tim', what='ham'))

TestTemplate = test_string.TestTemplate()
test_regular_templates_with_braces()
