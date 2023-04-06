import unittest
import string
from string import Template
import test_string

def test_name_lookup():
    fmt = string.Formatter()

    class AnyAttr:

        def __getattr__(ModuleTest, attr):
            return attr
    x = AnyAttr()
    ModuleTest.assertEqual(fmt.format('{0.lumber}{0.jack}', x), 'lumberjack')
    with ModuleTest.assertRaises(AttributeError):
        fmt.format('{0.lumber}{0.jack}', '')

ModuleTest = test_string.ModuleTest()
test_name_lookup()
