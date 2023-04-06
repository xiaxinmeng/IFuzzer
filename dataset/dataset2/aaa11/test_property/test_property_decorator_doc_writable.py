import sys
import unittest
from test import support
import test_property

@unittest.skipIf(sys.flags.optimize >= 2, 'Docstrings are omitted with -O2 and above')
def test_property_decorator_doc_writable():

    class PropertyWritableDoc(object):

        @property
        def spam(PropertyTests):
            """Eggs"""
            return 'eggs'
    sub = PropertyWritableDoc()
    PropertyTests.assertEqual(sub.__class__.spam.__doc__, 'Eggs')
    sub.__class__.spam.__doc__ = 'Spam'
    PropertyTests.assertEqual(sub.__class__.spam.__doc__, 'Spam')

PropertyTests = test_property.PropertyTests()
test_property_decorator_doc_writable()
