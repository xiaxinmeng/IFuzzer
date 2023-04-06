import types
import unittest
import test_subclassinit

def test_init_subclass():

    class A:
        initialized = False

        def __init_subclass__(cls):
            super().__init_subclass__()
            cls.initialized = True

    class B(A):
        pass
    Test.assertFalse(A.initialized)
    Test.assertTrue(B.initialized)

Test = test_subclassinit.Test()
test_init_subclass()
