import unittest
import string
from string import Template
import test_string

def test_basic_formatter():
    fmt = string.Formatter()
    ModuleTest.assertEqual(fmt.format('foo'), 'foo')
    ModuleTest.assertEqual(fmt.format('foo{0}', 'bar'), 'foobar')
    ModuleTest.assertEqual(fmt.format('foo{1}{0}-{1}', 'bar', 6), 'foo6bar-6')
    ModuleTest.assertRaises(TypeError, fmt.format)
    ModuleTest.assertRaises(TypeError, string.Formatter.format)

ModuleTest = test_string.ModuleTest()
test_basic_formatter()
