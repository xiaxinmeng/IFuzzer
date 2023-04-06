import unittest
import sys
import typing
import test_isinstance

def test_isinstance_abstract():
    TestIsInstanceIsSubclass.assertEqual(True, isinstance(test_isinstance.AbstractSuper(), test_isinstance.AbstractSuper))
    TestIsInstanceIsSubclass.assertEqual(False, isinstance(test_isinstance.AbstractSuper(),test_isinstance.AbstractChild))
    TestIsInstanceIsSubclass.assertEqual(False, isinstance(test_isinstance.AbstractSuper(), test_isinstance.Super))
    TestIsInstanceIsSubclass.assertEqual(False, isinstance(test_isinstance.AbstractSuper(), test_isinstance.Child))
    TestIsInstanceIsSubclass.assertEqual(True, isinstance(test_isinstance.AbstractChild(), test_isinstance.AbstractChild))
    TestIsInstanceIsSubclass.assertEqual(True, isinstance(test_isinstance.AbstractChild(), test_isinstance.AbstractSuper))
    TestIsInstanceIsSubclass.assertEqual(False, isinstance(test_isinstance.AbstractChild(), test_isinstance.Super))
    TestIsInstanceIsSubclass.assertEqual(False, isinstance(test_isinstance.AbstractChild(), test_isinstance.Child))

TestIsInstanceIsSubclass = test_isinstance.TestIsInstanceIsSubclass()
test_isinstance_abstract()
