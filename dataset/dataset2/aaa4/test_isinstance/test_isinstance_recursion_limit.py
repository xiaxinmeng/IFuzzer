import unittest
import sys
import typing
import test_isinstance

def test_isinstance_recursion_limit():
    TestIsInstanceIsSubclass.assertRaises(RecursionError, test_isinstance.blowstack, isinstance, '', str)

TestIsInstanceIsSubclass = test_isinstance.TestIsInstanceIsSubclass()
test_isinstance_recursion_limit()
