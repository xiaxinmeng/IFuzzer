import unittest
import string
from string import Template
import test_string

def test_regular_templates():
    s = Template('$who likes to eat a bag of $what worth $$100')
    TestTemplate.assertEqual(s.substitute(dict(who='tim', what='ham')), 'tim likes to eat a bag of ham worth $100')
    TestTemplate.assertRaises(KeyError, s.substitute, dict(who='tim'))
    TestTemplate.assertRaises(TypeError, Template.substitute)

TestTemplate = test_string.TestTemplate()
test_regular_templates()
