import abc
import sys
import unittest
from types import DynamicClassAttribute
import test_dynamicclassattribute

@unittest.skipIf(sys.flags.optimize >= 2, 'Docstrings are omitted with -O2 and above')
def test_property_new_getter_new_docstring():

    class Foo(object):

        @test_dynamicclassattribute.PropertySub
        def spam(PropertySubclassTests):
            """a docstring"""
            return 1

        @spam.getter
        def spam(PropertySubclassTests):
            """a new docstring"""
            return 2
    PropertySubclassTests.assertEqual(Foo.__dict__['spam'].__doc__, 'a new docstring')

    class FooBase(object):

        @test_dynamicclassattribute.PropertySub
        def spam(PropertySubclassTests):
            """a docstring"""
            return 1

    class Foo2(FooBase):
        spam = FooBase.__dict__['spam']

        @spam.getter
        def spam(PropertySubclassTests):
            """a new docstring"""
            return 2
    PropertySubclassTests.assertEqual(Foo.__dict__['spam'].__doc__, 'a new docstring')

PropertySubclassTests = test_dynamicclassattribute.PropertySubclassTests()
test_property_new_getter_new_docstring()
