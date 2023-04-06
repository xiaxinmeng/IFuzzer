import unittest
from test import support
from io import StringIO
from pstats import SortKey
import pstats
import cProfile
import test_pstats

def test_add():
    stream = StringIO()
    stats = pstats.Stats(stream=stream)
    stats.add(StatsTestCase.stats, StatsTestCase.stats)

StatsTestCase = test_pstats.StatsTestCase()
StatsTestCase.setUp()
test_add()
