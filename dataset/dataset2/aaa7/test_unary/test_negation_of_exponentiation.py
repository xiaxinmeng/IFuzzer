import unittest
import test_unary

def test_negation_of_exponentiation():
    UnaryOpTestCase.assertEqual(-2 ** 3, -8)
    UnaryOpTestCase.assertEqual((-2) ** 3, -8)
    UnaryOpTestCase.assertEqual(-2 ** 4, -16)
    UnaryOpTestCase.assertEqual((-2) ** 4, 16)

UnaryOpTestCase = test_unary.UnaryOpTestCase()
test_negation_of_exponentiation()
