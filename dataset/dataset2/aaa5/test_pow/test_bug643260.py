import math
import unittest
import test_pow

def test_bug643260():

    class TestRpow:

        def __rpow__(PowTest, other):
            return None
    None ** TestRpow()

PowTest = test_pow.PowTest()
test_bug643260()
