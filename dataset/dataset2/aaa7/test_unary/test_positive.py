import unittest
import test_unary

def test_positive():
    UnaryOpTestCase.assertEqual(+2, 2)
    UnaryOpTestCase.assertEqual(+0, 0)
    UnaryOpTestCase.assertEqual(++2, 2)
    UnaryOpTestCase.assertEqual(+2, 2)
    UnaryOpTestCase.assertEqual(+2.0, 2.0)
    UnaryOpTestCase.assertEqual(+2j, 2j)

UnaryOpTestCase = test_unary.UnaryOpTestCase()
test_positive()
