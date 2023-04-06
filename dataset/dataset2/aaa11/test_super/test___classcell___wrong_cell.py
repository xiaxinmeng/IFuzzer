import unittest
import test_super

def test___classcell___wrong_cell():

    class Meta(type):

        def __new__(cls, name, bases, namespace):
            cls = super().__new__(cls, name, bases, namespace)
            B = type('B', (), namespace)
            return cls
    with TestSuper.assertRaises(TypeError):

        class A(metaclass=Meta):

            def f(TestSuper):
                return __class__

TestSuper = test_super.TestSuper()
test___classcell___wrong_cell()
