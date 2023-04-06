import unittest
from test.support import import_helper
import types
import test_xxlimited

def test_new():
    xxo = CommonTests.module.new()
    CommonTests.assertEqual(xxo.demo('abc'), 'abc')

CommonTests = test_xxlimited.CommonTests()
test_new()
