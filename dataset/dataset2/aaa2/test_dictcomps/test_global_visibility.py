import unittest
import test_dictcomps
g = "Global variable"
def test_global_visibility():
    expected = {0: 'Global variable', 1: 'Global variable', 2: 'Global variable', 3: 'Global variable', 4: 'Global variable', 5: 'Global variable', 6: 'Global variable', 7: 'Global variable', 8: 'Global variable', 9: 'Global variable'}
    actual = {k: g for k in range(10)}
    DictComprehensionTest.assertEqual(actual, expected)

DictComprehensionTest = test_dictcomps.DictComprehensionTest()
test_global_visibility()
