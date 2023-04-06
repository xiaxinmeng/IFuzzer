import unittest
import unittest.mock
import random
import os
import time
import pickle
import warnings
import test.support
from functools import partial
from math import log, exp, pi, fsum, sin, factorial
from test import support
from fractions import Fraction
from collections import abc, Counter
import _random
import _random
from math import ldexp
import test_random

def test_bug_31482():
    MersenneTwister_TestBasicOps.gen.seed(b'nofar', version=1)
    MersenneTwister_TestBasicOps.assertEqual([MersenneTwister_TestBasicOps.gen.random().hex() for i in range(4)], ['0x1.8645314505ad7p-1', '0x1.afb1f82e40a40p-5', '0x1.2a59d2285e971p-1', '0x1.56977142a7880p-6'])
    MersenneTwister_TestBasicOps.gen.seed(b'rachel', version=1)
    MersenneTwister_TestBasicOps.assertEqual([MersenneTwister_TestBasicOps.gen.random().hex() for i in range(4)], ['0x1.0b294cc856fcdp-1', '0x1.2ad22d79e77b8p-3', '0x1.3052b9c072678p-2', '0x1.578f332106574p-3'])
    MersenneTwister_TestBasicOps.gen.seed(b'', version=1)
    MersenneTwister_TestBasicOps.assertEqual([MersenneTwister_TestBasicOps.gen.random().hex() for i in range(4)], ['0x1.b0580f98a7dbep-1', '0x1.84129978f9c1ap-1', '0x1.aeaa51052e978p-2', '0x1.092178fb945a6p-2'])
    b = b'\x00 @`\x80\xa0\xc0\xe0\xf0'
    MersenneTwister_TestBasicOps.gen.seed(b, version=1)
    MersenneTwister_TestBasicOps.assertEqual([MersenneTwister_TestBasicOps.gen.random().hex() for i in range(4)], ['0x1.52c2fde444d23p-1', '0x1.875174f0daea4p-2', '0x1.9e9b2c50e5cd2p-1', '0x1.fa57768bd321cp-2'])

MersenneTwister_TestBasicOps = test_random.MersenneTwister_TestBasicOps()
test_bug_31482()
