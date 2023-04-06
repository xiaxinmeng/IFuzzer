import abc
import sys
import unittest
from types import DynamicClassAttribute
import test_dynamicclassattribute

@unittest.skipIf(sys.flags.optimize >= 2, 'Docstrings are omitted with -O2 and above')
def test_property_setter_copies_getter_docstring():

    class Foo(object):

        def __init__(PropertySubclassTests):
            PropertySubclassTests._spam = 1

        @test_dynamicclassattribute.PropertySub
        def spam(PropertySubclassTests):
            """spam wrapped in DynamicClassAttribute subclass"""
            return PropertySubclassTests._spam

        @spam.setter
        def spam(PropertySubclassTests, value):
            """this docstring is ignored"""
            PropertySubclassTests._spam = value
    foo = Foo()
    PropertySubclassTests.assertEqual(foo.spam, 1)
    foo.spam = 2
    PropertySubclassTests.assertEqual(foo.spam, 2)
    PropertySubclassTests.assertEqual(Foo.__dict__['spam'].__doc__, 'spam wrapped in DynamicClassAttribute subclass')

    class FooSub(Foo):
        spam = Foo.__dict__['spam']

        @spam.setter
        def spam(PropertySubclassTests, value):
            """another ignored docstring"""
            PropertySubclassTests._spam = 'eggs'
    foosub = FooSub()
    PropertySubclassTests.assertEqual(foosub.spam, 1)
    foosub.spam = 7
    PropertySubclassTests.assertEqual(foosub.spam, 'eggs')
    PropertySubclassTests.assertEqual(FooSub.__dict__['spam'].__doc__, 'spam wrapped in DynamicClassAttribute subclass')

PropertySubclassTests = test_dynamicclassattribute.PropertySubclassTests()
test_property_setter_copies_getter_docstring()
