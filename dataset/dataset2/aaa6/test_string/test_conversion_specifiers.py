import unittest
import string
from string import Template
import test_string

def test_conversion_specifiers():
    fmt = string.Formatter()
    ModuleTest.assertEqual(fmt.format('-{arg!r}-', arg='test'), "-'test'-")
    ModuleTest.assertEqual(fmt.format('{0!s}', 'test'), 'test')
    ModuleTest.assertRaises(ValueError, fmt.format, '{0!h}', 'test')
    ModuleTest.assertEqual(fmt.format('{0!a}', 42), '42')
    ModuleTest.assertEqual(fmt.format('{0!a}', string.ascii_letters), "'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'")
    ModuleTest.assertEqual(fmt.format('{0!a}', chr(255)), "'\\xff'")
    ModuleTest.assertEqual(fmt.format('{0!a}', chr(256)), "'\\u0100'")

ModuleTest = test_string.ModuleTest()
test_conversion_specifiers()
