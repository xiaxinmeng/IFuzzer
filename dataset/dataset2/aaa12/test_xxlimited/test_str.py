import unittest
from test.support import import_helper
import types
import test_xxlimited

def test_str():
    CommonTests.assertTrue(issubclass(CommonTests.module.Str, str))
    CommonTests.assertIsNot(CommonTests.module.Str, str)
    custom_string = CommonTests.module.Str('abcd')
    CommonTests.assertEqual(custom_string, 'abcd')
    CommonTests.assertEqual(custom_string.upper(), 'ABCD')

CommonTests = test_xxlimited.CommonTests()
test_str()
