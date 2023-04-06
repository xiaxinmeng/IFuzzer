import unittest
from test.support import import_helper
import types
import test_xxlimited

def test_xxo_attributes():
    xxo = CommonTests.module.Xxo()
    with CommonTests.assertRaises(AttributeError):
        xxo.foo
    with CommonTests.assertRaises(AttributeError):
        del xxo.foo
    xxo.foo = 1234
    CommonTests.assertEqual(xxo.foo, 1234)
    del xxo.foo
    with CommonTests.assertRaises(AttributeError):
        xxo.foo

CommonTests = test_xxlimited.CommonTests()
test_xxo_attributes()
