import sys
import unittest
from test import support
from test.test_grammar import VALID_UNDERSCORE_LITERALS, INVALID_UNDERSCORE_LITERALS
from array import array
import test_int

def test_issue31619():
    IntTestCases.assertEqual(int('1_0_1_0_1_0_1_0_1_0_1_0_1_0_1_0_1_0_1_0_1_0_1_0_1_0_1_0_1_0_1', 2), 1431655765)
    IntTestCases.assertEqual(int('1_2_3_4_5_6_7_0_1_2_3', 8), 1402433619)
    IntTestCases.assertEqual(int('1_2_3_4_5_6_7_8_9', 16), 4886718345)
    IntTestCases.assertEqual(int('1_2_3_4_5_6_7', 32), 1144132807)

IntTestCases = test_int.IntTestCases()
test_issue31619()
