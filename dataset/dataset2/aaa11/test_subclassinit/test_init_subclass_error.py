import types
import unittest
import test_subclassinit

def test_init_subclass_error():

    class A:

        def __init_subclass__(cls):
            raise RuntimeError
    with Test.assertRaises(RuntimeError):

        class B(A):
            pass

Test = test_subclassinit.Test()
test_init_subclass_error()
