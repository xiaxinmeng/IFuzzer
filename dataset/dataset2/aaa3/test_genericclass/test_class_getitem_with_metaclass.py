import unittest
from test import support
from _testcapi import Generic, GenericAlias
import test_genericclass

def test_class_getitem_with_metaclass():

    class Meta(type):
        pass

    class C(metaclass=Meta):

        def __class_getitem__(cls, item):
            return f'{cls.__name__}[{item.__name__}]'
    TestClassGetitem.assertEqual(C[int], 'C[int]')

TestClassGetitem = test_genericclass.TestClassGetitem()
test_class_getitem_with_metaclass()
