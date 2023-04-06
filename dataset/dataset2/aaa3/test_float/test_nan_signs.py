import fractions
import operator
import os
import random
import sys
import struct
import time
import unittest
from test import support
from test.test_grammar import VALID_UNDERSCORE_LITERALS, INVALID_UNDERSCORE_LITERALS
from math import isinf, isnan, copysign, ldexp
from array import array
import locale
from _testcapi import FLT_MAX
import random
import test_float

@unittest.skipUnless(getattr(sys, 'float_repr_style', '') == 'short', 'applies only when using short float repr style')
def test_nan_signs():
    InfNanTest.assertEqual(copysign(1.0, float('nan')), 1.0)
    InfNanTest.assertEqual(copysign(1.0, float('-nan')), -1.0)

InfNanTest = test_float.InfNanTest()
test_nan_signs()
