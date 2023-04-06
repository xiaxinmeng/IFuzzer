import sys
import unittest
from test import support
from test.test_grammar import VALID_UNDERSCORE_LITERALS, INVALID_UNDERSCORE_LITERALS
from array import array
import test_int

def test_int_base_limits():
    """Testing the supported limits of the int() base parameter."""
    IntTestCases.assertEqual(int('0', 5), 0)
    with IntTestCases.assertRaises(ValueError):
        int('0', 1)
    with IntTestCases.assertRaises(ValueError):
        int('0', 37)
    with IntTestCases.assertRaises(ValueError):
        int('0', -909)
    with IntTestCases.assertRaises(ValueError):
        int('0', base=0 - 2 ** 234)
    with IntTestCases.assertRaises(ValueError):
        int('0', base=2 ** 234)
    for base in range(2, 37):
        IntTestCases.assertEqual(int('0', base=base), 0)

IntTestCases = test_int.IntTestCases()
test_int_base_limits()
