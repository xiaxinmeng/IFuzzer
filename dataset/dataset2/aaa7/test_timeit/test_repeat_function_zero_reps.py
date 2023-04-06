import timeit
import unittest
import sys
import io
from textwrap import dedent
from test.support import captured_stdout
from test.support import captured_stderr
import test_timeit

def test_repeat_function_zero_reps():
    delta_times = timeit.repeat(TestTimeit.fake_stmt, TestTimeit.fake_setup, repeat=0, timer=test_timeit.FakeTimer())
    TestTimeit.assertEqual(delta_times, [])

TestTimeit = test_timeit.TestTimeit()
test_repeat_function_zero_reps()
