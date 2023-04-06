import unittest
import sys
import typing
import test_isinstance

def test_subclass_normal():
    TestIsInstanceIsSubclass.assertEqual(True, issubclass(test_isinstance.Super, test_isinstance.Super))
    TestIsInstanceIsSubclass.assertEqual(False, issubclass(test_isinstance.Super, test_isinstance.AbstractSuper))
    TestIsInstanceIsSubclass.assertEqual(False, issubclass(test_isinstance.Super, test_isinstance.Child))
    TestIsInstanceIsSubclass.assertEqual(True, issubclass(test_isinstance.Child, test_isinstance.Child))
    TestIsInstanceIsSubclass.assertEqual(True, issubclass(test_isinstance.Child, test_isinstance.Super))
    TestIsInstanceIsSubclass.assertEqual(False, issubclass(test_isinstance.Child, test_isinstance.AbstractSuper))
    TestIsInstanceIsSubclass.assertTrue(issubclass(typing.List, typing.List | typing.Tuple))
    TestIsInstanceIsSubclass.assertFalse(issubclass(int, typing.List | typing.Tuple))

TestIsInstanceIsSubclass = test_isinstance.TestIsInstanceIsSubclass()
test_subclass_normal()
