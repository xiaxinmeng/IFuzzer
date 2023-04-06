import unittest
import string
from string import Template
import test_string

def test_override_format_field():

    class CallFormatter(string.Formatter):

        def format_field(ModuleTest, value, format_spec):
            return format(value(), format_spec)
    fmt = CallFormatter()
    ModuleTest.assertEqual(fmt.format('*{0}*', lambda : 'result'), '*result*')

ModuleTest = test_string.ModuleTest()
test_override_format_field()
