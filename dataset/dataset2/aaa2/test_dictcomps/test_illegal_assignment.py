import unittest
import test_dictcomps

def test_illegal_assignment():
    with DictComprehensionTest.assertRaisesRegex(SyntaxError, 'cannot assign'):
        compile('{x: y for y, x in ((1, 2), (3, 4))} = 5', '<test>', 'exec')
    with DictComprehensionTest.assertRaisesRegex(SyntaxError, 'illegal expression'):
        compile('{x: y for y, x in ((1, 2), (3, 4))} += 5', '<test>', 'exec')

DictComprehensionTest = test_dictcomps.DictComprehensionTest()
test_illegal_assignment()
