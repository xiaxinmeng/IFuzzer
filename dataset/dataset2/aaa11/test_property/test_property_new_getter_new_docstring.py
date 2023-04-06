import sys
import unittest
from test import support
import test_property

@unittest.skipIf(sys.flags.optimize >= 2, 'Docstrings are omitted with -O2 and above')
def test_property_new_getter_new_docstring():

    class Foo(object):

        @test_property.PropertySub
        def spam(PropertySubclassTests):
            """a docstring"""
            return 1

        @spam.getter
        def spam(PropertySubclassTests):
            """a new docstring"""
            return 2
    PropertySubclassTests.assertEqual(Foo.spam.__doc__, 'a new docstring')

    class FooBase(object):

        @test_property.PropertySub
        def spam(PropertySubclassTests):
            """a docstring"""
            return 1

    class Foo2(FooBase):

        @FooBase.spam.getter
        def spam(PropertySubclassTests):
            """a new docstring"""
            return 2
    PropertySubclassTests.assertEqual(Foo.spam.__doc__, 'a new docstring')

PropertySubclassTests = test_property.PropertySubclassTests()
test_property_new_getter_new_docstring()
