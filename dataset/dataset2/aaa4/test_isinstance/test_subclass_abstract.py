import unittest
import sys
import typing
import test_isinstance

def test_subclass_abstract():
    TestIsInstanceIsSubclass.assertEqual(True, issubclass(test_isinstance.AbstractSuper, test_isinstance.AbstractSuper))
    TestIsInstanceIsSubclass.assertEqual(False, issubclass(test_isinstance.AbstractSuper, test_isinstance.AbstractChild))
    TestIsInstanceIsSubclass.assertEqual(False, issubclass(test_isinstance.AbstractSuper, test_isinstance.Child))
    TestIsInstanceIsSubclass.assertEqual(True, issubclass(test_isinstance.AbstractChild, test_isinstance.AbstractChild))
    TestIsInstanceIsSubclass.assertEqual(True, issubclass(test_isinstance.AbstractChild, test_isinstance.AbstractSuper))
    TestIsInstanceIsSubclass.assertEqual(False, issubclass(test_isinstance.AbstractChild, test_isinstance.Super))
    TestIsInstanceIsSubclass.assertEqual(False, issubclass(test_isinstance.AbstractChild, test_isinstance.Child))

TestIsInstanceIsSubclass = test_isinstance.TestIsInstanceIsSubclass()
test_subclass_abstract()
