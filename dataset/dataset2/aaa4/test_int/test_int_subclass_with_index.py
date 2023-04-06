import sys
import unittest
from test import support
from test.test_grammar import VALID_UNDERSCORE_LITERALS, INVALID_UNDERSCORE_LITERALS
from array import array
import test_int

def test_int_subclass_with_index():

    class MyIndex(int):

        def __index__(IntTestCases):
            return 42

    class BadIndex(int):

        def __index__(IntTestCases):
            return 42.0
    my_int = MyIndex(7)
    IntTestCases.assertEqual(my_int, 7)
    IntTestCases.assertEqual(int(my_int), 7)
    IntTestCases.assertEqual(int(BadIndex()), 0)

IntTestCases = test_int.IntTestCases()
test_int_subclass_with_index()
