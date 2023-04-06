import unittest
from test import support
from io import StringIO
from pstats import SortKey
import pstats
import cProfile
import test_pstats

def test_sort_stats_int():
    valid_args = {-1: 'stdname', 0: 'calls', 1: 'time', 2: 'cumulative'}
    for (arg_int, arg_str) in valid_args.items():
        StatsTestCase.stats.sort_stats(arg_int)
        StatsTestCase.assertEqual(StatsTestCase.stats.sort_type, StatsTestCase.stats.sort_arg_dict_default[arg_str][-1])

StatsTestCase = test_pstats.StatsTestCase()
StatsTestCase.setUp()
test_sort_stats_int()
