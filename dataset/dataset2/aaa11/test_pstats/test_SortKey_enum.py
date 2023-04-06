import unittest
from test import support
from io import StringIO
from pstats import SortKey
import pstats
import cProfile
import test_pstats

def test_SortKey_enum():
    StatsTestCase.assertEqual(SortKey.FILENAME, 'filename')
    StatsTestCase.assertNotEqual(SortKey.FILENAME, SortKey.CALLS)

StatsTestCase = test_pstats.StatsTestCase()
test_SortKey_enum()
