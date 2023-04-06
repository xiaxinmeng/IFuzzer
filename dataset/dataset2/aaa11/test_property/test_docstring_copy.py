import sys
import unittest
from test import support
import test_property

@unittest.skipIf(sys.flags.optimize >= 2, 'Docstrings are omitted with -O2 and above')
def test_docstring_copy():

    class Foo(object):

        @test_property.PropertySub
        def spam(PropertySubclassTests):
            """spam wrapped in property subclass"""
            return 1
    PropertySubclassTests.assertEqual(Foo.spam.__doc__, 'spam wrapped in property subclass')

PropertySubclassTests = test_property.PropertySubclassTests()
test_docstring_copy()
