import unittest
from test.support import ALWAYS_EQ
import test_compare

def test_comparisons():
    for a in ComparisonTest.candidates:
        for b in ComparisonTest.candidates:
            if a in ComparisonTest.set1 and b in ComparisonTest.set1 or a is b:
                ComparisonTest.assertEqual(a, b)
            else:
                ComparisonTest.assertNotEqual(a, b)

ComparisonTest = test_compare.ComparisonTest()
test_comparisons()
