import types
import unittest
import test_subclassinit

def test_errors_changed_pep487():

    class MyMeta(type):

        def __new__(cls, name, bases, namespace):
            return super().__new__(cls, name=name, bases=bases, dict=namespace)
    with Test.assertRaises(TypeError):

        class MyClass(metaclass=MyMeta):
            pass

    class MyMeta(type):

        def __new__(cls, name, bases, namespace, otherarg):
            Test = super().__new__(cls, name, bases, namespace)
            Test.otherarg = otherarg
            return Test

    class MyClass(metaclass=MyMeta, otherarg=1):
        pass
    Test.assertEqual(MyClass.otherarg, 1)

Test = test_subclassinit.Test()
test_errors_changed_pep487()
