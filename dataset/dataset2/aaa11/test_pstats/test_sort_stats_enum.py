import unittest
from test import support
from io import StringIO
from pstats import SortKey
import pstats
import cProfile
import test_pstats

def test_sort_stats_enum():
    for member in SortKey:
        StatsTestCase.stats.sort_stats(member)
        StatsTestCase.assertEqual(StatsTestCase.stats.sort_type, StatsTestCase.stats.sort_arg_dict_default[member.value][-1])

StatsTestCase = test_pstats.StatsTestCase()
StatsTestCase.setUp()
test_sort_stats_enum()
