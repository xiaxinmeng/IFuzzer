import unittest
import sys
import typing
import test_isinstance

def test_subclass_recursion_limit():
    TestIsInstanceIsSubclass.assertRaises(RecursionError, test_isinstance.blowstack, issubclass, str, str)

TestIsInstanceIsSubclass = test_isinstance.TestIsInstanceIsSubclass()
test_subclass_recursion_limit()
