import unittest
import test_dictcomps

def test_star_expression():
    expected = {0: 0, 1: 1, 2: 4, 3: 9}
    DictComprehensionTest.assertEqual({i: i * i for i in [*range(4)]}, expected)
    DictComprehensionTest.assertEqual({i: i * i for i in (*range(4),)}, expected)

DictComprehensionTest = test_dictcomps.DictComprehensionTest()
test_star_expression()
