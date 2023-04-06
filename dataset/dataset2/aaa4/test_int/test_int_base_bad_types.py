import sys
import unittest
from test import support
from test.test_grammar import VALID_UNDERSCORE_LITERALS, INVALID_UNDERSCORE_LITERALS
from array import array
import test_int

def test_int_base_bad_types():
    """Not integer types are not valid bases; issue16772."""
    with IntTestCases.assertRaises(TypeError):
        int('0', 5.5)
    with IntTestCases.assertRaises(TypeError):
        int('0', 5.0)

IntTestCases = test_int.IntTestCases()
test_int_base_bad_types()
