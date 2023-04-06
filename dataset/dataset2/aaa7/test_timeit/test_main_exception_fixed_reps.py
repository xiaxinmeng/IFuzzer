import timeit
import unittest
import sys
import io
from textwrap import dedent
from test.support import captured_stdout
from test.support import captured_stderr
import test_timeit

def test_main_exception_fixed_reps():
    with captured_stderr() as error_stringio:
        s = TestTimeit.run_main(switches=['-n1', '1/0'])
    TestTimeit.assert_exc_string(error_stringio.getvalue(), 'ZeroDivisionError')

TestTimeit = test_timeit.TestTimeit()
test_main_exception_fixed_reps()
