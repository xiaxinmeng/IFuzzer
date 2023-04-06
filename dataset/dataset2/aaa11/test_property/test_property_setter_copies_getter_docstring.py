import sys
import unittest
from test import support
import test_property

@unittest.skipIf(sys.flags.optimize >= 2, 'Docstrings are omitted with -O2 and above')
def test_property_setter_copies_getter_docstring():

    class Foo(object):

        def __init__(PropertySubclassTests):
            PropertySubclassTests._spam = 1

        @test_property.PropertySub
        def spam(PropertySubclassTests):
            """spam wrapped in property subclass"""
            return PropertySubclassTests._spam

        @spam.setter
        def spam(PropertySubclassTests, value):
            """this docstring is ignored"""
            PropertySubclassTests._spam = value
    foo = Foo()
    PropertySubclassTests.assertEqual(foo.spam, 1)
    foo.spam = 2
    PropertySubclassTests.assertEqual(foo.spam, 2)
    PropertySubclassTests.assertEqual(Foo.spam.__doc__, 'spam wrapped in property subclass')

    class FooSub(Foo):

        @Foo.spam.setter
        def spam(PropertySubclassTests, value):
            """another ignored docstring"""
            PropertySubclassTests._spam = 'eggs'
    foosub = FooSub()
    PropertySubclassTests.assertEqual(foosub.spam, 1)
    foosub.spam = 7
    PropertySubclassTests.assertEqual(foosub.spam, 'eggs')
    PropertySubclassTests.assertEqual(FooSub.spam.__doc__, 'spam wrapped in property subclass')

PropertySubclassTests = test_property.PropertySubclassTests()
test_property_setter_copies_getter_docstring()
