import timeit
import unittest
import sys
import io
from textwrap import dedent
from test.support import captured_stdout
from test.support import captured_stderr
import test_timeit

def test_main_microseconds():
    s = TestTimeit.run_main(seconds_per_increment=2.5e-06, switches=['-n100'])
    TestTimeit.assertEqual(s, '100 loops, best of 5: 2.5 usec per loop\n')

TestTimeit = test_timeit.TestTimeit()
test_main_microseconds()
