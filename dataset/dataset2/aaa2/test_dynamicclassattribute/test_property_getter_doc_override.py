import abc
import sys
import unittest
from types import DynamicClassAttribute
import test_dynamicclassattribute

@unittest.skipIf(sys.flags.optimize >= 2, 'Docstrings are omitted with -O2 and above')
def test_property_getter_doc_override():
    newgettersub = test_dynamicclassattribute.PropertySubNewGetter()
    PropertyTests.assertEqual(newgettersub.spam, 5)
    PropertyTests.assertEqual(newgettersub.__class__.__dict__['spam'].__doc__, 'new docstring')
    newgetter = test_dynamicclassattribute.PropertyNewGetter()
    PropertyTests.assertEqual(newgetter.spam, 8)
    PropertyTests.assertEqual(newgetter.__class__.__dict__['spam'].__doc__, 'new docstring')

PropertyTests = test_dynamicclassattribute.PropertyTests()
test_property_getter_doc_override()
