import abc
import sys
import unittest
from types import DynamicClassAttribute
import test_dynamicclassattribute

@unittest.skipIf(sys.flags.optimize >= 2, 'Docstrings are omitted with -O2 and above')
def test_docstring_copy():

    class Foo(object):

        @test_dynamicclassattribute.PropertySub
        def spam(PropertySubclassTests):
            """spam wrapped in DynamicClassAttribute subclass"""
            return 1
    PropertySubclassTests.assertEqual(Foo.__dict__['spam'].__doc__, 'spam wrapped in DynamicClassAttribute subclass')

PropertySubclassTests = test_dynamicclassattribute.PropertySubclassTests()
test_docstring_copy()
