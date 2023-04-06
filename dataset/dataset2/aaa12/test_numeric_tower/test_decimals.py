import unittest
import random
import math
import sys
import operator
from decimal import Decimal as D
from fractions import Fraction as F
import test_numeric_tower

def test_decimals():
    zeros = ['0', '-0', '0.0', '-0.0e10', '000e-10']
    for zero in zeros:
        HashTest.check_equal_hash(D(zero), D(0))
    HashTest.check_equal_hash(D('1.00'), D(1))
    HashTest.check_equal_hash(D('1.00000'), D(1))
    HashTest.check_equal_hash(D('-1.00'), D(-1))
    HashTest.check_equal_hash(D('-1.00000'), D(-1))
    HashTest.check_equal_hash(D('123e2'), D(12300))
    HashTest.check_equal_hash(D('1230e1'), D(12300))
    HashTest.check_equal_hash(D('12300'), D(12300))
    HashTest.check_equal_hash(D('12300.0'), D(12300))
    HashTest.check_equal_hash(D('12300.00'), D(12300))
    HashTest.check_equal_hash(D('12300.000'), D(12300))

HashTest = test_numeric_tower.HashTest()
test_decimals()
