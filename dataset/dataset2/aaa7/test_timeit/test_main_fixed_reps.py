import timeit
import unittest
import sys
import io
from textwrap import dedent
from test.support import captured_stdout
from test.support import captured_stderr
import test_timeit

def test_main_fixed_reps():
    s = TestTimeit.run_main(seconds_per_increment=60.0, switches=['-r9'])
    TestTimeit.assertEqual(s, '1 loop, best of 9: 60 sec per loop\n')

TestTimeit = test_timeit.TestTimeit()
test_main_fixed_reps()
