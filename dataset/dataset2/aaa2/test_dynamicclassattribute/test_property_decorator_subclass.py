import abc
import sys
import unittest
from types import DynamicClassAttribute
import test_dynamicclassattribute

def test_property_decorator_subclass():
    sub = test_dynamicclassattribute.SubClass()
    PropertyTests.assertRaises(test_dynamicclassattribute.PropertyGet, getattr, sub, 'spam')
    PropertyTests.assertRaises(test_dynamicclassattribute.PropertySet, setattr, sub, 'spam', None)
    PropertyTests.assertRaises(test_dynamicclassattribute.PropertyDel, delattr, sub, 'spam')

PropertyTests = test_dynamicclassattribute.PropertyTests()
test_property_decorator_subclass()
