import timeit
import unittest
import sys
import io
from textwrap import dedent
from test.support import captured_stdout
from test.support import captured_stderr
import test_timeit

def test_main_very_verbose():
    s = TestTimeit.run_main(seconds_per_increment=3e-05, switches=['-vv'])
    TestTimeit.assertEqual(s, dedent('                1 loop -> 3e-05 secs\n                2 loops -> 6e-05 secs\n                5 loops -> 0.00015 secs\n                10 loops -> 0.0003 secs\n                20 loops -> 0.0006 secs\n                50 loops -> 0.0015 secs\n                100 loops -> 0.003 secs\n                200 loops -> 0.006 secs\n                500 loops -> 0.015 secs\n                1000 loops -> 0.03 secs\n                2000 loops -> 0.06 secs\n                5000 loops -> 0.15 secs\n                10000 loops -> 0.3 secs\n\n                raw times: 300 msec, 300 msec, 300 msec, 300 msec, 300 msec\n\n                10000 loops, best of 5: 30 usec per loop\n            '))

TestTimeit = test_timeit.TestTimeit()
test_main_very_verbose()
