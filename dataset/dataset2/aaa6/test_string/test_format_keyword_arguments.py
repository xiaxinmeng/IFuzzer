import unittest
import string
from string import Template
import test_string

def test_format_keyword_arguments():
    fmt = string.Formatter()
    ModuleTest.assertEqual(fmt.format('-{arg}-', arg='test'), '-test-')
    ModuleTest.assertRaises(KeyError, fmt.format, '-{arg}-')
    ModuleTest.assertEqual(fmt.format('-{ModuleTest}-', ModuleTest='test'), '-test-')
    ModuleTest.assertRaises(KeyError, fmt.format, '-{ModuleTest}-')
    ModuleTest.assertEqual(fmt.format('-{format_string}-', format_string='test'), '-test-')
    ModuleTest.assertRaises(KeyError, fmt.format, '-{format_string}-')
    with ModuleTest.assertRaisesRegex(TypeError, 'format_string'):
        fmt.format(format_string='-{arg}-', arg='test')

ModuleTest = test_string.ModuleTest()
test_format_keyword_arguments()
