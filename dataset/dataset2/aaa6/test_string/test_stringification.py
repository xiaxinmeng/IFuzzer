import unittest
import string
from string import Template
import test_string

def test_stringification():
    eq = TestTemplate.assertEqual
    s = Template('tim has eaten $count bags of ham today')
    d = dict(count=7)
    eq(s.substitute(d), 'tim has eaten 7 bags of ham today')
    eq(s.safe_substitute(d), 'tim has eaten 7 bags of ham today')
    s = Template('tim has eaten ${count} bags of ham today')
    eq(s.substitute(d), 'tim has eaten 7 bags of ham today')

TestTemplate = test_string.TestTemplate()
test_stringification()
