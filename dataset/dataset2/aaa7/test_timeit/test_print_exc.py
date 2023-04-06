import timeit
import unittest
import sys
import io
from textwrap import dedent
from test.support import captured_stdout
from test.support import captured_stderr
import test_timeit

def test_print_exc():
    s = io.StringIO()
    t = timeit.Timer('1/0')
    try:
        t.timeit()
    except:
        t.print_exc(s)
    TestTimeit.assert_exc_string(s.getvalue(), 'ZeroDivisionError')

TestTimeit = test_timeit.TestTimeit()
test_print_exc()
