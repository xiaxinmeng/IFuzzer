import timeit
import unittest
import sys
import io
from textwrap import dedent
from test.support import captured_stdout
from test.support import captured_stderr
import test_timeit

def test_main_seconds():
    s = TestTimeit.run_main(seconds_per_increment=5.5)
    TestTimeit.assertEqual(s, '1 loop, best of 5: 5.5 sec per loop\n')

TestTimeit = test_timeit.TestTimeit()
test_main_seconds()
