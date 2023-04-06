import abc
import sys
import unittest
from types import DynamicClassAttribute
import test_dynamicclassattribute

def test_property_decorator_baseclass():
    base = test_dynamicclassattribute.BaseClass()
    PropertyTests.assertEqual(base.spam, 5)
    PropertyTests.assertEqual(base._spam, 5)
    base.spam = 10
    PropertyTests.assertEqual(base.spam, 10)
    PropertyTests.assertEqual(base._spam, 10)
    delattr(base, 'spam')
    PropertyTests.assertTrue(not hasattr(base, 'spam'))
    PropertyTests.assertTrue(not hasattr(base, '_spam'))
    base.spam = 20
    PropertyTests.assertEqual(base.spam, 20)
    PropertyTests.assertEqual(base._spam, 20)

PropertyTests = test_dynamicclassattribute.PropertyTests()
test_property_decorator_baseclass()
