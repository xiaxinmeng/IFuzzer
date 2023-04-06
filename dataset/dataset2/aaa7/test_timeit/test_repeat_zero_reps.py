import timeit
import unittest
import sys
import io
from textwrap import dedent
from test.support import captured_stdout
from test.support import captured_stderr
import test_timeit

def test_repeat_zero_reps():
    TestTimeit.repeat(TestTimeit.fake_stmt, TestTimeit.fake_setup, repeat=0)

TestTimeit = test_timeit.TestTimeit()
test_repeat_zero_reps()
