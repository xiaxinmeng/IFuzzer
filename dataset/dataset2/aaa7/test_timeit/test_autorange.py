import timeit
import unittest
import sys
import io
from textwrap import dedent
from test.support import captured_stdout
from test.support import captured_stderr
import test_timeit

def test_autorange():
    (num_loops, time_taken) = TestTimeit.autorange()
    TestTimeit.assertEqual(num_loops, 500)
    TestTimeit.assertEqual(time_taken, 500 / 1024)

TestTimeit = test_timeit.TestTimeit()
test_autorange()
