import unittest
from itertools import repeat
from collections import deque
from operator import length_hint
import test_iterlen

def test_issue1242657():
    TestLengthHintExceptions.assertRaises(RuntimeError, list, test_iterlen.BadLen())
    TestLengthHintExceptions.assertRaises(RuntimeError, list, test_iterlen.BadLengthHint())
    TestLengthHintExceptions.assertRaises(RuntimeError, [].extend, test_iterlen.BadLen())
    TestLengthHintExceptions.assertRaises(RuntimeError, [].extend, test_iterlen.BadLengthHint())
    b = bytearray(range(10))
    TestLengthHintExceptions.assertRaises(RuntimeError, b.extend, test_iterlen.BadLen())
    TestLengthHintExceptions.assertRaises(RuntimeError, b.extend, test_iterlen.BadLengthHint())

TestLengthHintExceptions = test_iterlen.TestLengthHintExceptions()
test_issue1242657()
