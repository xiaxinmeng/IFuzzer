import unittest
from test import support
from _testcapi import Generic, GenericAlias
import test_genericclass

def test_class_getitem_patched():

    class C:

        def __init_subclass__(cls):

            def __class_getitem__(cls, item):
                return f'{cls.__name__}[{item.__name__}]'
            cls.__class_getitem__ = classmethod(__class_getitem__)

    class D(C):
        ...
    TestClassGetitem.assertEqual(D[int], 'D[int]')
    TestClassGetitem.assertEqual(D[D], 'D[D]')

TestClassGetitem = test_genericclass.TestClassGetitem()
test_class_getitem_patched()
