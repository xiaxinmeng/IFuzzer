import timeit
import unittest
import sys
import io
from textwrap import dedent
from test.support import captured_stdout
from test.support import captured_stderr
import test_timeit

def test_main_multiple_setups():
    s = TestTimeit.run_main(seconds_per_increment=2.0, switches=['-n35', '-s', 'a = "CustomSetup"', '-s', 'print(a)'])
    TestTimeit.assertEqual(s, 'CustomSetup\n' * DEFAULT_REPEAT + '35 loops, best of 5: 2 sec per loop\n')

DEFAULT_REPEAT = 5
TestTimeit = test_timeit.TestTimeit()
test_main_multiple_setups()
