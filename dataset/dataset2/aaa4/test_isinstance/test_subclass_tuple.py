import unittest
import sys
import typing
import test_isinstance

def test_subclass_tuple():
    TestIsInstanceIsSubclass.assertEqual(True, issubclass(test_isinstance.Child, (test_isinstance.Child,)))
    TestIsInstanceIsSubclass.assertEqual(True, issubclass(test_isinstance.Child, (test_isinstance.Super,)))
    TestIsInstanceIsSubclass.assertEqual(False, issubclass(test_isinstance.Super, (test_isinstance.Child,)))
    TestIsInstanceIsSubclass.assertEqual(True, issubclass(test_isinstance.Super, (test_isinstance.Child, test_isinstance.Super)))
    TestIsInstanceIsSubclass.assertEqual(False, issubclass(test_isinstance.Child, ()))
    TestIsInstanceIsSubclass.assertEqual(True, issubclass(test_isinstance.Super, (test_isinstance.Child, (test_isinstance.Super,))))
    TestIsInstanceIsSubclass.assertEqual(True, issubclass(int, (int, (float, int))))
    TestIsInstanceIsSubclass.assertEqual(True, issubclass(str, (str, (test_isinstance.Child, str))))

TestIsInstanceIsSubclass = test_isinstance.TestIsInstanceIsSubclass()
test_subclass_tuple()
