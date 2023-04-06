import abc
import sys
import unittest
from types import DynamicClassAttribute
import test_dynamicclassattribute

@unittest.skipIf(sys.flags.optimize >= 2, 'Docstrings are omitted with -O2 and above')
def test_property_decorator_subclass_doc():
    sub = test_dynamicclassattribute.SubClass()
    PropertyTests.assertEqual(sub.__class__.__dict__['spam'].__doc__, 'SubClass.getter')

PropertyTests = test_dynamicclassattribute.PropertyTests()
test_property_decorator_subclass_doc()
