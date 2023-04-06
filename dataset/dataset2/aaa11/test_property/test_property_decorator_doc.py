import sys
import unittest
from test import support
import test_property

def test_property_decorator_doc():
    base = test_property.PropertyDocBase()
    sub = test_property.PropertyDocSub()
    PropertyTests.assertEqual(base.__class__.spam.__doc__, 'spam spam spam')
    PropertyTests.assertEqual(sub.__class__.spam.__doc__, 'spam spam spam')

PropertyTests = test_property.PropertyTests()
test_property_decorator_doc()
