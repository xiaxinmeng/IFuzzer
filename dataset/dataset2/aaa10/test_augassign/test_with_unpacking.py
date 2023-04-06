import unittest
import test_augassign

def test_with_unpacking():
    AugAssignTest.assertRaises(SyntaxError, compile, 'x, b += 3', '<test>', 'exec')

AugAssignTest = test_augassign.AugAssignTest()
test_with_unpacking()
