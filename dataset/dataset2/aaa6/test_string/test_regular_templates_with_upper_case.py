import unittest
import string
from string import Template
import test_string

def test_regular_templates_with_upper_case():
    s = Template('$WHO likes ${WHAT} for ${MEAL}')
    d = dict(WHO='tim', WHAT='ham', MEAL='dinner')
    TestTemplate.assertEqual(s.substitute(d), 'tim likes ham for dinner')

TestTemplate = test_string.TestTemplate()
test_regular_templates_with_upper_case()
