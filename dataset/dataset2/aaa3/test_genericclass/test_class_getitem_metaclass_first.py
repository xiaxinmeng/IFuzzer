import unittest
from test import support
from _testcapi import Generic, GenericAlias
import test_genericclass

def test_class_getitem_metaclass_first():

    class Meta(type):

        def __getitem__(cls, item):
            return 'from metaclass'

    class C(metaclass=Meta):

        def __class_getitem__(cls, item):
            return 'from __class_getitem__'
    TestClassGetitem.assertEqual(C[int], 'from metaclass')

TestClassGetitem = test_genericclass.TestClassGetitem()
test_class_getitem_metaclass_first()
