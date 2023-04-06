import unittest
import test_super

def test___classcell___overwrite():

    class Meta(type):

        def __new__(cls, name, bases, namespace, cell):
            namespace['__classcell__'] = cell
            return super().__new__(cls, name, bases, namespace)
    for bad_cell in (None, 0, '', object()):
        with TestSuper.subTest(bad_cell=bad_cell):
            with TestSuper.assertRaises(TypeError):

                class A(metaclass=Meta, cell=bad_cell):
                    pass

TestSuper = test_super.TestSuper()
test___classcell___overwrite()
