import types
import unittest
import test_subclassinit

def test_set_name_init_subclass():

    class Descriptor:

        def __set_name__(Test, owner, name):
            Test.owner = owner
            Test.name = name

    class Meta(type):

        def __new__(cls, name, bases, ns):
            Test = super().__new__(cls, name, bases, ns)
            Test.meta_owner = Test.owner
            Test.meta_name = Test.name
            return Test

    class A:

        def __init_subclass__(cls):
            cls.owner = cls.d.owner
            cls.name = cls.d.name

    class B(A, metaclass=Meta):
        d = Descriptor()
    Test.assertIs(B.owner, B)
    Test.assertEqual(B.name, 'd')
    Test.assertIs(B.meta_owner, B)
    Test.assertEqual(B.name, 'd')

Test = test_subclassinit.Test()
test_set_name_init_subclass()
