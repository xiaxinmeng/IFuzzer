import abc
import sys
import unittest
from types import DynamicClassAttribute
import test_dynamicclassattribute

def test_property_decorator_doc():
    base = test_dynamicclassattribute.PropertyDocBase()
    sub = test_dynamicclassattribute.PropertyDocSub()
    PropertyTests.assertEqual(base.__class__.__dict__['spam'].__doc__, 'spam spam spam')
    PropertyTests.assertEqual(sub.__class__.__dict__['spam'].__doc__, 'spam spam spam')

PropertyTests = test_dynamicclassattribute.PropertyTests()
test_property_decorator_doc()
