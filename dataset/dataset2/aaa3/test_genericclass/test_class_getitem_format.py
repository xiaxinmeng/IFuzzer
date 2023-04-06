import unittest
from test import support
from _testcapi import Generic, GenericAlias
import test_genericclass

def test_class_getitem_format():

    class C:

        def __class_getitem__(cls, item):
            return f'C[{item.__name__}]'
    TestClassGetitem.assertEqual(C[int], 'C[int]')
    TestClassGetitem.assertEqual(C[C], 'C[C]')

TestClassGetitem = test_genericclass.TestClassGetitem()
test_class_getitem_format()
