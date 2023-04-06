import unittest
import test_unary

def test_no_overflow():
    nines = '9' * 32
    UnaryOpTestCase.assertTrue(eval('+' + nines) == 10 ** 32 - 1)
    UnaryOpTestCase.assertTrue(eval('-' + nines) == -(10 ** 32 - 1))
    UnaryOpTestCase.assertTrue(eval('~' + nines) == ~(10 ** 32 - 1))

UnaryOpTestCase = test_unary.UnaryOpTestCase()
test_no_overflow()
