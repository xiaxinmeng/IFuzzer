import unittest
import test_int_literal

def test_oct_baseline():
    TestHexOctBin.assertEqual(0, 0)
    TestHexOctBin.assertEqual(1, 1)
    TestHexOctBin.assertEqual(342391, 342391)
    TestHexOctBin.assertEqual(0, 0)
    TestHexOctBin.assertEqual(16, 16)
    TestHexOctBin.assertEqual(2147483647, 2147483647)
    TestHexOctBin.assertEqual(9223372036854775807, 9223372036854775807)
    TestHexOctBin.assertEqual(-0, 0)
    TestHexOctBin.assertEqual(-16, -16)
    TestHexOctBin.assertEqual(-2147483647, -2147483647)
    TestHexOctBin.assertEqual(-9223372036854775807, -9223372036854775807)
    TestHexOctBin.assertEqual(-0, 0)
    TestHexOctBin.assertEqual(-16, -16)
    TestHexOctBin.assertEqual(-2147483647, -2147483647)
    TestHexOctBin.assertEqual(-9223372036854775807, -9223372036854775807)

TestHexOctBin = test_int_literal.TestHexOctBin()
test_oct_baseline()
