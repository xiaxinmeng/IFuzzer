import unittest
import string
from string import Template
import test_string

def test_index_lookup():
    fmt = string.Formatter()
    lookup = ['eggs', 'and', 'spam']
    ModuleTest.assertEqual(fmt.format('{0[2]}{0[0]}', lookup), 'spameggs')
    with ModuleTest.assertRaises(IndexError):
        fmt.format('{0[2]}{0[0]}', [])
    with ModuleTest.assertRaises(KeyError):
        fmt.format('{0[2]}{0[0]}', {})

ModuleTest = test_string.ModuleTest()
test_index_lookup()
