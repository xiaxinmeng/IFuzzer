import timeit
import unittest
import sys
import io
from textwrap import dedent
from test.support import captured_stdout
from test.support import captured_stderr
import test_timeit

def test_repeat_function_zero_iters():
    delta_times = timeit.repeat(TestTimeit.fake_stmt, TestTimeit.fake_setup, number=0, timer=test_timeit.FakeTimer())
    TestTimeit.assertEqual(delta_times, DEFAULT_REPEAT * [0.0])

DEFAULT_REPEAT = 5
TestTimeit = test_timeit.TestTimeit()
test_repeat_function_zero_iters()
