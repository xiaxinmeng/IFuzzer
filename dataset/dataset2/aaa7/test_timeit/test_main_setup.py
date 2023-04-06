import timeit
import unittest
import sys
import io
from textwrap import dedent
from test.support import captured_stdout
from test.support import captured_stderr
import test_timeit
DEFAULT_REPEAT = 5
def test_main_setup():
    s = TestTimeit.run_main(seconds_per_increment=2.0, switches=['-n35', '-s', 'print("CustomSetup")'])
    TestTimeit.assertEqual(s, 'CustomSetup\n' * DEFAULT_REPEAT + '35 loops, best of 5: 2 sec per loop\n')

TestTimeit = test_timeit.TestTimeit()
test_main_setup()
