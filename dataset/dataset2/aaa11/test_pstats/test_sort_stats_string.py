import unittest
from test import support
from io import StringIO
from pstats import SortKey
import pstats
import cProfile
import test_pstats

def test_sort_stats_string():
    for sort_name in ['calls', 'ncalls', 'cumtime', 'cumulative', 'filename', 'line', 'module', 'name', 'nfl', 'pcalls', 'stdname', 'time', 'tottime']:
        StatsTestCase.stats.sort_stats(sort_name)
        StatsTestCase.assertEqual(StatsTestCase.stats.sort_type, StatsTestCase.stats.sort_arg_dict_default[sort_name][-1])

StatsTestCase = test_pstats.StatsTestCase()
StatsTestCase.setUp()
test_sort_stats_string()
