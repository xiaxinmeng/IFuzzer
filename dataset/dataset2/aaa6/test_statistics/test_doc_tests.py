import bisect
import collections
import collections.abc
import copy
import decimal
import doctest
import math
import pickle
import random
import sys
import unittest
from test import support
from test.support import import_helper
from decimal import Decimal
from fractions import Fraction
import statistics
import test_statistics

@unittest.skipIf(sys.flags.optimize >= 2, 'Docstrings are omitted with -OO and above')
def test_doc_tests():
    (failed, tried) = doctest.testmod(statistics, optionflags=doctest.ELLIPSIS)
    DocTests.assertGreater(tried, 0)
    DocTests.assertEqual(failed, 0)

DocTests = test_statistics.DocTests()
test_doc_tests()
