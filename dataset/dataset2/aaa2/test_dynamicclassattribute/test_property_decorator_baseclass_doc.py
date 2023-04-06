import abc
import sys
import unittest
from types import DynamicClassAttribute
import test_dynamicclassattribute

@unittest.skipIf(sys.flags.optimize >= 2, 'Docstrings are omitted with -O2 and above')
def test_property_decorator_baseclass_doc():
    base = test_dynamicclassattribute.BaseClass()
    PropertyTests.assertEqual(base.__class__.__dict__['spam'].__doc__, 'BaseClass.getter')

PropertyTests = test_dynamicclassattribute.PropertyTests()
test_property_decorator_baseclass_doc()
