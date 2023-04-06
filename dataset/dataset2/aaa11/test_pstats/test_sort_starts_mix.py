import unittest
from test import support
from io import StringIO
from pstats import SortKey
import pstats
import cProfile
import test_pstats

def test_sort_starts_mix():
    StatsTestCase.assertRaises(TypeError, StatsTestCase.stats.sort_stats, 'calls', SortKey.TIME)
    StatsTestCase.assertRaises(TypeError, StatsTestCase.stats.sort_stats, SortKey.TIME, 'calls')

StatsTestCase = test_pstats.StatsTestCase()
StatsTestCase.setUp()
test_sort_starts_mix()
