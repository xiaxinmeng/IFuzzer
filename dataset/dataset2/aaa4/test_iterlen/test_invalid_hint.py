import unittest
from itertools import repeat
from collections import deque
from operator import length_hint
import test_iterlen

def test_invalid_hint():
    TestLengthHintExceptions.assertEqual(list(test_iterlen.NoneLengthHint()), list(range(10)))

TestLengthHintExceptions = test_iterlen.TestLengthHintExceptions()
test_invalid_hint()
