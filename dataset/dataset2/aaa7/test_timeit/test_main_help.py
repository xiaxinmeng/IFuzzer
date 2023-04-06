import timeit
import unittest
import sys
import io
from textwrap import dedent
from test.support import captured_stdout
from test.support import captured_stderr
import test_timeit

@unittest.skipIf(sys.flags.optimize >= 2, 'need __doc__')
def test_main_help():
    s = TestTimeit.run_main(switches=['-h'])
    TestTimeit.assertEqual(s, timeit.__doc__ + ' ')

TestTimeit = test_timeit.TestTimeit()
test_main_help()
