import unittest
import test_int_literal

def test_oct_unsigned():
    TestHexOctBin.assertEqual(2147483648, 2147483648)
    TestHexOctBin.assertEqual(4294967295, 4294967295)
    TestHexOctBin.assertEqual(-2147483648, -2147483648)
    TestHexOctBin.assertEqual(-4294967295, -4294967295)
    TestHexOctBin.assertEqual(-2147483648, -2147483648)
    TestHexOctBin.assertEqual(-4294967295, -4294967295)
    TestHexOctBin.assertEqual(9223372036854775808, 9223372036854775808)
    TestHexOctBin.assertEqual(18446744073709551615, 18446744073709551615)
    TestHexOctBin.assertEqual(-9223372036854775808, -9223372036854775808)
    TestHexOctBin.assertEqual(-18446744073709551615, -18446744073709551615)
    TestHexOctBin.assertEqual(-9223372036854775808, -9223372036854775808)
    TestHexOctBin.assertEqual(-18446744073709551615, -18446744073709551615)

TestHexOctBin = test_int_literal.TestHexOctBin()
test_oct_unsigned()
