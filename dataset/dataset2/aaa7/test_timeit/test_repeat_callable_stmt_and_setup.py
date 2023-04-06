import timeit
import unittest
import sys
import io
from textwrap import dedent
from test.support import captured_stdout
from test.support import captured_stderr
import test_timeit

def test_repeat_callable_stmt_and_setup():
    TestTimeit.repeat(TestTimeit.fake_callable_stmt, TestTimeit.fake_callable_setup, repeat=3, number=5)

TestTimeit = test_timeit.TestTimeit()
test_repeat_callable_stmt_and_setup()
