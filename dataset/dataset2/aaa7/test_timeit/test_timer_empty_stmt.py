import timeit
import unittest
import sys
import io
from textwrap import dedent
from test.support import captured_stdout
from test.support import captured_stderr
import test_timeit

def test_timer_empty_stmt():
    timeit.Timer(stmt='')
    timeit.Timer(stmt=' \n\t\x0c')
    timeit.Timer(stmt='# comment')

TestTimeit = test_timeit.TestTimeit()
test_timer_empty_stmt()
