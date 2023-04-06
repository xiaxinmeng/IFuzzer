import types
import unittest
import test_subclassinit

def test_init_subclass_wrong():

    class A:

        def __init_subclass__(cls, whatever):
            pass
    with Test.assertRaises(TypeError):

        class B(A):
            pass

Test = test_subclassinit.Test()
test_init_subclass_wrong()
