import unittest
from test.support import ALWAYS_EQ
import test_compare

def test_ne_defaults_to_not_eq():
    a = test_compare.Cmp(1)
    b = test_compare.Cmp(1)
    c = test_compare.Cmp(2)
    ComparisonTest.assertIs(a == b, True)
    ComparisonTest.assertIs(a != b, False)
    ComparisonTest.assertIs(a != c, True)

ComparisonTest = test_compare.ComparisonTest()
test_ne_defaults_to_not_eq()
