import timeit
import unittest
import sys
import io
from textwrap import dedent
from test.support import captured_stdout
from test.support import captured_stderr
import test_timeit

def test_main_milliseconds():
    s = TestTimeit.run_main(seconds_per_increment=0.0055)
    TestTimeit.assertEqual(s, '50 loops, best of 5: 5.5 msec per loop\n')

TestTimeit = test_timeit.TestTimeit()
test_main_milliseconds()
