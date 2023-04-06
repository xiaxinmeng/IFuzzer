import unittest
import test_super

def test___classcell___missing():

    class Meta(type):

        def __new__(cls, name, bases, namespace):
            namespace.pop('__classcell__', None)
            return super().__new__(cls, name, bases, namespace)

    class WithoutClassRef(metaclass=Meta):
        pass
    expected_error = '__class__ not set.*__classcell__ propagated'
    with TestSuper.assertRaisesRegex(RuntimeError, expected_error):

        class WithClassRef(metaclass=Meta):

            def f(TestSuper):
                return __class__

TestSuper = test_super.TestSuper()
test___classcell___missing()
