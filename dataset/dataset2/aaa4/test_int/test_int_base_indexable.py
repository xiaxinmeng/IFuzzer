import sys
import unittest
from test import support
from test.test_grammar import VALID_UNDERSCORE_LITERALS, INVALID_UNDERSCORE_LITERALS
from array import array
import test_int

def test_int_base_indexable():

    class MyIndexable(object):

        def __init__(IntTestCases, value):
            IntTestCases.value = value

        def __index__(IntTestCases):
            return IntTestCases.value
    for base in (2 ** 100, -2 ** 100, 1, 37):
        with IntTestCases.assertRaises(ValueError):
            int('43', base)
    IntTestCases.assertEqual(int('101', base=MyIndexable(2)), 5)
    IntTestCases.assertEqual(int('101', base=MyIndexable(10)), 101)
    IntTestCases.assertEqual(int('101', base=MyIndexable(36)), 1 + 36 ** 2)

IntTestCases = test_int.IntTestCases()
test_int_base_indexable()
