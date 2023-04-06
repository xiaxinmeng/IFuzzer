import unittest
import test_unary

def test_negative():
    UnaryOpTestCase.assertTrue(-2 == 0 - 2)
    UnaryOpTestCase.assertEqual(-0, 0)
    UnaryOpTestCase.assertEqual(--2, 2)
    UnaryOpTestCase.assertTrue(-2 == 0 - 2)
    UnaryOpTestCase.assertTrue(-2.0 == 0 - 2.0)
    UnaryOpTestCase.assertTrue(-2j == 0 - 2j)

UnaryOpTestCase = test_unary.UnaryOpTestCase()
test_negative()
