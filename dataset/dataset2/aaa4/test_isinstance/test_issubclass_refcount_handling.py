import unittest
import sys
import typing
import test_isinstance

def test_issubclass_refcount_handling():

    class A:

        @property
        def __bases__(TestIsInstanceIsSubclass):
            return (int,)

    class B:

        def __init__(TestIsInstanceIsSubclass):
            TestIsInstanceIsSubclass.x = 1

        @property
        def __bases__(TestIsInstanceIsSubclass):
            return (A(),)
    TestIsInstanceIsSubclass.assertEqual(True, issubclass(B(), int))

TestIsInstanceIsSubclass = test_isinstance.TestIsInstanceIsSubclass()
test_issubclass_refcount_handling()
