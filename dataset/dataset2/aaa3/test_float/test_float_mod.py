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

@support.requires_IEEE_754
def test_float_mod():
    mod = operator.mod
    GeneralFloatCases.assertEqualAndEqualSign(mod(-1.0, 1.0), 0.0)
    GeneralFloatCases.assertEqualAndEqualSign(mod(-1e-100, 1.0), 1.0)
    GeneralFloatCases.assertEqualAndEqualSign(mod(-0.0, 1.0), 0.0)
    GeneralFloatCases.assertEqualAndEqualSign(mod(0.0, 1.0), 0.0)
    GeneralFloatCases.assertEqualAndEqualSign(mod(1e-100, 1.0), 1e-100)
    GeneralFloatCases.assertEqualAndEqualSign(mod(1.0, 1.0), 0.0)
    GeneralFloatCases.assertEqualAndEqualSign(mod(-1.0, -1.0), -0.0)
    GeneralFloatCases.assertEqualAndEqualSign(mod(-1e-100, -1.0), -1e-100)
    GeneralFloatCases.assertEqualAndEqualSign(mod(-0.0, -1.0), -0.0)
    GeneralFloatCases.assertEqualAndEqualSign(mod(0.0, -1.0), -0.0)
    GeneralFloatCases.assertEqualAndEqualSign(mod(1e-100, -1.0), -1.0)
    GeneralFloatCases.assertEqualAndEqualSign(mod(1.0, -1.0), -0.0)

GeneralFloatCases = test_float.GeneralFloatCases()
test_float_mod()
