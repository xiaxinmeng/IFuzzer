import unittest
from test import support
from _testcapi import Generic, GenericAlias
import test_genericclass

def test_class_getitem_with_builtins():

    class A(dict):
        called_with = None

        def __class_getitem__(cls, item):
            cls.called_with = item

    class B(A):
        pass
    TestClassGetitem.assertIs(B.called_with, None)
    B[int]
    TestClassGetitem.assertIs(B.called_with, int)

TestClassGetitem = test_genericclass.TestClassGetitem()
test_class_getitem_with_builtins()
