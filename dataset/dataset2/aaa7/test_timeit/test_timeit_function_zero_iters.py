import timeit
import unittest
import sys
import io
from textwrap import dedent
from test.support import captured_stdout
from test.support import captured_stderr
import test_timeit

def test_timeit_function_zero_iters():
    delta_time = timeit.timeit(TestTimeit.fake_stmt, TestTimeit.fake_setup, number=0, timer=test_timeit.FakeTimer())
    TestTimeit.assertEqual(delta_time, 0)

TestTimeit = test_timeit.TestTimeit()
test_timeit_function_zero_iters()
