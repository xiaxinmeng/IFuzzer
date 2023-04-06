import unittest
import random
import math
import sys
import operator
from decimal import Decimal as D
from fractions import Fraction as F
import test_numeric_tower
_PyHASH_MODULUS = sys.hash_info.modulus
_PyHASH_INF = sys.hash_info.inf
def test_fractions():
    HashTest.assertEqual(hash(F(1, _PyHASH_MODULUS)), _PyHASH_INF)
    HashTest.assertEqual(hash(F(-1, 3 * _PyHASH_MODULUS)), -_PyHASH_INF)
    HashTest.assertEqual(hash(F(7 * _PyHASH_MODULUS, 1)), 0)
    HashTest.assertEqual(hash(F(-_PyHASH_MODULUS, 1)), 0)

HashTest = test_numeric_tower.HashTest()
test_fractions()
