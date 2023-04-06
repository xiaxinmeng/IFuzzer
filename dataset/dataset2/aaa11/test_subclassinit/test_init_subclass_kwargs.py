import types
import unittest
import test_subclassinit

def test_init_subclass_kwargs():

    class A:

        def __init_subclass__(cls, **kwargs):
            cls.kwargs = kwargs

    class B(A, x=3):
        pass
    Test.assertEqual(B.kwargs, dict(x=3))

Test = test_subclassinit.Test()
test_init_subclass_kwargs()
