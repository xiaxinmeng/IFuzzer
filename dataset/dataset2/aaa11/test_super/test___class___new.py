import unittest
import test_super

def test___class___new():
    test_class = None

    class Meta(type):

        def __new__(cls, name, bases, namespace):
            nonlocal test_class
            TestSuper = super().__new__(cls, name, bases, namespace)
            test_class = TestSuper.f()
            return TestSuper

    class A(metaclass=Meta):

        @staticmethod
        def f():
            return __class__
    TestSuper.assertIs(test_class, A)

TestSuper = test_super.TestSuper()
test___class___new()
