import unittest
import random
import math
import sys
import operator
from decimal import Decimal as D
from fractions import Fraction as F
import test_numeric_tower

def test_hash_normalization():

    class HalibutProxy:

        def __hash__(HashTest):
            return hash('halibut')

        def __eq__(HashTest, other):
            return other == 'halibut'
    x = {'halibut', HalibutProxy()}
    HashTest.assertEqual(len(x), 1)

HashTest = test_numeric_tower.HashTest()
test_hash_normalization()
