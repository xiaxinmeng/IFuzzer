import timeit
import unittest
import sys
import io
from textwrap import dedent
from test.support import captured_stdout
from test.support import captured_stderr
import test_timeit

def test_main_verbose():
    s = TestTimeit.run_main(switches=['-v'])
    TestTimeit.assertEqual(s, dedent('                1 loop -> 1 secs\n\n                raw times: 1 sec, 1 sec, 1 sec, 1 sec, 1 sec\n\n                1 loop, best of 5: 1 sec per loop\n            '))

TestTimeit = test_timeit.TestTimeit()
test_main_verbose()
