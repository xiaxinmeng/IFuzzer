import unittest
import test_augassign

def test_Basic():
    x = 2
    x += 1
    x *= 2
    x **= 2
    x -= 8
    x //= 5
    x %= 3
    x &= 2
    x |= 5
    x ^= 1
    x /= 2
    AugAssignTest.assertEqual(x, 3.0)

AugAssignTest = test_augassign.AugAssignTest()
test_Basic()
