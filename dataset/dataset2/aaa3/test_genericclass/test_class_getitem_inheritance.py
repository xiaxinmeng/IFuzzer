import unittest
from test import support
from _testcapi import Generic, GenericAlias
import test_genericclass

def test_class_getitem_inheritance():

    class C:

        def __class_getitem__(cls, item):
            return f'{cls.__name__}[{item.__name__}]'

    class D(C):
        ...
    TestClassGetitem.assertEqual(D[int], 'D[int]')
    TestClassGetitem.assertEqual(D[D], 'D[D]')

TestClassGetitem = test_genericclass.TestClassGetitem()
test_class_getitem_inheritance()
