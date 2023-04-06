import sys
import unittest
from test import support
import test_property

def test_property_decorator_subclass():
    sub = test_property.SubClass()
    PropertyTests.assertRaises(test_property.PropertyGet, getattr, sub, 'spam')
    PropertyTests.assertRaises(test_property.PropertySet, setattr, sub, 'spam', None)
    PropertyTests.assertRaises(test_property.PropertyDel, delattr, sub, 'spam')

PropertyTests = test_property.PropertyTests()
test_property_decorator_subclass()
