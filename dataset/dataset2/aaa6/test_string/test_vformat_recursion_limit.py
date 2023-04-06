import unittest
import string
from string import Template
import test_string

def test_vformat_recursion_limit():
    fmt = string.Formatter()
    args = ()
    kwargs = dict(i=100)
    with ModuleTest.assertRaises(ValueError) as err:
        fmt._vformat('{i}', args, kwargs, set(), -1)
    ModuleTest.assertIn('recursion', str(err.exception))

ModuleTest = test_string.ModuleTest()
test_vformat_recursion_limit()
