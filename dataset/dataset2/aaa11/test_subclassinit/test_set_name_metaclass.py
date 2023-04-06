import types
import unittest
import test_subclassinit

def test_set_name_metaclass():

    class Meta(type):

        def __new__(cls, name, bases, ns):
            ret = super().__new__(cls, name, bases, ns)
            Test.assertEqual(ret.d.name, 'd')
            Test.assertIs(ret.d.owner, ret)
            return 0

    class Descriptor:

        def __set_name__(Test, owner, name):
            Test.owner = owner
            Test.name = name

    class A(metaclass=Meta):
        d = Descriptor()
    Test.assertEqual(A, 0)

Test = test_subclassinit.Test()
test_set_name_metaclass()
