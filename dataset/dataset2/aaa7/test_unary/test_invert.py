import unittest
import test_unary

def test_invert():
    UnaryOpTestCase.assertTrue(-2 == 0 - 2)
    UnaryOpTestCase.assertEqual(-0, 0)
    UnaryOpTestCase.assertEqual(--2, 2)
    UnaryOpTestCase.assertTrue(-2 == 0 - 2)

UnaryOpTestCase = test_unary.UnaryOpTestCase()
test_invert()
