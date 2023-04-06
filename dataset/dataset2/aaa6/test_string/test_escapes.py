import unittest
import string
from string import Template
import test_string

def test_escapes():
    eq = TestTemplate.assertEqual
    s = Template('$who likes to eat a bag of $$what worth $$100')
    eq(s.substitute(dict(who='tim', what='ham')), 'tim likes to eat a bag of $what worth $100')
    s = Template('$who likes $$')
    eq(s.substitute(dict(who='tim', what='ham')), 'tim likes $')

TestTemplate = test_string.TestTemplate()
test_escapes()
