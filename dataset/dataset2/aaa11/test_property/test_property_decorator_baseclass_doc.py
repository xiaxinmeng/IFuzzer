import sys
import unittest
from test import support
import test_property

@unittest.skipIf(sys.flags.optimize >= 2, 'Docstrings are omitted with -O2 and above')
def test_property_decorator_baseclass_doc():
    base = test_property.BaseClass()
    PropertyTests.assertEqual(base.__class__.spam.__doc__, 'BaseClass.getter')

PropertyTests = test_property.PropertyTests()
test_property_decorator_baseclass_doc()
