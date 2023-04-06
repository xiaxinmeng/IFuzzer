import unittest
from test.support import import_helper
import types
import test_xxlimited

def test_xxo_demo():
    xxo = TestXXLimited.module.Xxo()
    other = TestXXLimited.module.Xxo()
    TestXXLimited.assertEqual(xxo.demo('abc'), 'abc')
    TestXXLimited.assertEqual(xxo.demo(0), None)

TestXXLimited = test_xxlimited.TestXXLimited()
test_xxo_demo()
