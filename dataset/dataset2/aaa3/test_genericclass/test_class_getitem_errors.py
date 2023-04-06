import unittest
from test import support
from _testcapi import Generic, GenericAlias
import test_genericclass

def test_class_getitem_errors():

    class C_too_few:

        def __class_getitem__(cls):
            return None
    with TestClassGetitem.assertRaises(TypeError):
        C_too_few[int]

    class C_too_many:

        def __class_getitem__(cls, one, two):
            return None
    with TestClassGetitem.assertRaises(TypeError):
        C_too_many[int]

TestClassGetitem = test_genericclass.TestClassGetitem()
test_class_getitem_errors()
