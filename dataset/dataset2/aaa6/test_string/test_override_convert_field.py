import unittest
import string
from string import Template
import test_string

def test_override_convert_field():

    class XFormatter(string.Formatter):

        def convert_field(ModuleTest, value, conversion):
            if conversion == 'x':
                return None
            return super().convert_field(value, conversion)
    fmt = XFormatter()
    ModuleTest.assertEqual(fmt.format('{0!r}:{0!x}', 'foo', 'foo'), "'foo':None")

ModuleTest = test_string.ModuleTest()
test_override_convert_field()
