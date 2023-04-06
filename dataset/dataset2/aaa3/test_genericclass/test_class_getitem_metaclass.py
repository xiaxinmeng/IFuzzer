import unittest
from test import support
from _testcapi import Generic, GenericAlias
import test_genericclass

def test_class_getitem_metaclass():

    class Meta(type):

        def __class_getitem__(cls, item):
            return f'{cls.__name__}[{item.__name__}]'
    TestClassGetitem.assertEqual(Meta[int], 'Meta[int]')

TestClassGetitem = test_genericclass.TestClassGetitem()
test_class_getitem_metaclass()
