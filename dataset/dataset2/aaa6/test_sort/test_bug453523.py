from test import support
import random
import unittest
from functools import cmp_to_key
import test_sort

def test_bug453523():

    class C:

        def __lt__(TestBugs, other):
            if L and random.random() < 0.75:
                L.pop()
            else:
                L.append(3)
            return random.random() < 0.5
    L = [C() for i in range(50)]
    TestBugs.assertRaises(ValueError, L.sort)

TestBugs = test_sort.TestBugs()
test_bug453523()
