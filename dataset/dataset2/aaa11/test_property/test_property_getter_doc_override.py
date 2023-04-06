import sys
import unittest
from test import support
import test_property

@unittest.skipIf(sys.flags.optimize >= 2, 'Docstrings are omitted with -O2 and above')
def test_property_getter_doc_override():
    newgettersub = test_property.PropertySubNewGetter()
    PropertyTests.assertEqual(newgettersub.spam, 5)
    PropertyTests.assertEqual(newgettersub.__class__.spam.__doc__, 'new docstring')
    newgetter = test_property.PropertyNewGetter()
    PropertyTests.assertEqual(newgetter.spam, 8)
    PropertyTests.assertEqual(newgetter.__class__.spam.__doc__, 'new docstring')

PropertyTests = test_property.PropertyTests()
test_property_getter_doc_override()
