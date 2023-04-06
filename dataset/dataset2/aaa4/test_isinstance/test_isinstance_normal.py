import unittest
import sys
import typing
import test_isinstance

def test_isinstance_normal():
    TestIsInstanceIsSubclass.assertEqual(True, isinstance(test_isinstance.Super(), test_isinstance.Super))
    TestIsInstanceIsSubclass.assertEqual(False, isinstance(test_isinstance.Super(),test_isinstance.Child))
    TestIsInstanceIsSubclass.assertEqual(False, isinstance(test_isinstance.Super(), test_isinstance.AbstractSuper))
    TestIsInstanceIsSubclass.assertEqual(False, isinstance(test_isinstance.Super(), test_isinstance.AbstractChild))
    TestIsInstanceIsSubclass.assertEqual(True, isinstance(test_isinstance.Child(), test_isinstance.Super))
    TestIsInstanceIsSubclass.assertEqual(False, isinstance(test_isinstance.Child(), test_isinstance.AbstractSuper))

TestIsInstanceIsSubclass = test_isinstance.TestIsInstanceIsSubclass()
test_isinstance_normal()
