import sys
import unittest
from test import support
import test_property

@unittest.skipIf(sys.flags.optimize >= 2, 'Docstrings are omitted with -O2 and above')
def test_property_builtin_doc_writable():
    p = property(doc='basic')
    PropertyTests.assertEqual(p.__doc__, 'basic')
    p.__doc__ = 'extended'
    PropertyTests.assertEqual(p.__doc__, 'extended')

PropertyTests = test_property.PropertyTests()
PropertyTests.setUp()
test_property_builtin_doc_writable()
