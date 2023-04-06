import unittest
import test_augassign

def test_InDict():
    x = {0: 2}
    x[0] += 1
    x[0] *= 2
    x[0] **= 2
    x[0] -= 8
    x[0] //= 5
    x[0] %= 3
    x[0] &= 2
    x[0] |= 5
    x[0] ^= 1
    x[0] /= 2
    AugAssignTest.assertEqual(x[0], 3.0)

AugAssignTest = test_augassign.AugAssignTest()
test_InDict()
