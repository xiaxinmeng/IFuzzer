import sys
import unittest
from test import support
import test_property

@unittest.skipIf(sys.flags.optimize >= 2, 'Docstrings are omitted with -O2 and above')
def test_property_decorator_subclass_doc():
    sub = test_property.SubClass()
    PropertyTests.assertEqual(sub.__class__.spam.__doc__, 'SubClass.getter')

PropertyTests = test_property.PropertyTests()
test_property_decorator_subclass_doc()
