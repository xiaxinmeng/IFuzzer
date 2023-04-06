import timeit
import unittest
import sys
import io
from textwrap import dedent
from test.support import captured_stdout
from test.support import captured_stderr
import test_timeit

def test_autorange_second():
    (num_loops, time_taken) = TestTimeit.autorange(seconds_per_increment=1.0)
    TestTimeit.assertEqual(num_loops, 1)
    TestTimeit.assertEqual(time_taken, 1.0)

TestTimeit = test_timeit.TestTimeit()
test_autorange_second()
