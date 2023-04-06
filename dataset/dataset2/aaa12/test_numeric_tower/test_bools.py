import unittest
import random
import math
import sys
import operator
from decimal import Decimal as D
from fractions import Fraction as F
import test_numeric_tower

def test_bools():
    HashTest.check_equal_hash(False, 0)
    HashTest.check_equal_hash(True, 1)

HashTest = test_numeric_tower.HashTest()
test_bools()
