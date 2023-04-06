import unittest
import string
from string import Template
import test_string

def test_unicode_values():
    s = Template('$who likes $what')
    d = dict(who='tÿm', what='fþ\x0ced')
    TestTemplate.assertEqual(s.substitute(d), 'tÿm likes fþ\x0ced')

TestTemplate = test_string.TestTemplate()
test_unicode_values()
