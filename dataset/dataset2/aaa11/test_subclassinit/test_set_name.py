import types
import unittest
import test_subclassinit

def test_set_name():

    class Descriptor:

        def __set_name__(Test, owner, name):
            Test.owner = owner
            Test.name = name

    class A:
        d = Descriptor()
    Test.assertEqual(A.d.name, 'd')
    Test.assertIs(A.d.owner, A)

Test = test_subclassinit.Test()
test_set_name()
