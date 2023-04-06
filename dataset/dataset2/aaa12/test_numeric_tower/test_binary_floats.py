import unittest
import random
import math
import sys
import operator
from decimal import Decimal as D
from fractions import Fraction as F
import test_numeric_tower

def test_binary_floats():
    HashTest.check_equal_hash(0.0, -0.0)
    HashTest.check_equal_hash(0.0, D(0))
    HashTest.check_equal_hash(-0.0, D(0))
    HashTest.check_equal_hash(-0.0, D('-0.0'))
    HashTest.check_equal_hash(0.0, F(0))
    HashTest.check_equal_hash(float('inf'), D('inf'))
    HashTest.check_equal_hash(float('-inf'), D('-inf'))
    for _ in range(1000):
        x = random.random() * math.exp(random.random() * 200.0 - 100.0)
        HashTest.check_equal_hash(x, D.from_float(x))
        HashTest.check_equal_hash(x, F.from_float(x))

HashTest = test_numeric_tower.HashTest()
test_binary_floats()
