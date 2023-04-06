import unittest
from test.support import import_helper
import types
import test_xxlimited

def test_foo():
    CommonTests.assertEqual(CommonTests.module.foo(1, 2), 3)

CommonTests = test_xxlimited.CommonTests()
test_foo()
