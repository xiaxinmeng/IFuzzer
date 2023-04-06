import unittest
import test_dictcomps

def test_local_visibility():
    v = 'Local variable'
    expected = {0: 'Local variable', 1: 'Local variable', 2: 'Local variable', 3: 'Local variable', 4: 'Local variable', 5: 'Local variable', 6: 'Local variable', 7: 'Local variable', 8: 'Local variable', 9: 'Local variable'}
    actual = {k: v for k in range(10)}
    DictComprehensionTest.assertEqual(actual, expected)
    DictComprehensionTest.assertEqual(v, 'Local variable')

DictComprehensionTest = test_dictcomps.DictComprehensionTest()
test_local_visibility()
