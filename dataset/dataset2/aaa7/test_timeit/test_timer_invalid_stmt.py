import timeit
import unittest
import sys
import io
from textwrap import dedent
from test.support import captured_stdout
from test.support import captured_stderr
import test_timeit

def test_timer_invalid_stmt():
    TestTimeit.assertRaises(ValueError, timeit.Timer, stmt=None)
    TestTimeit.assertRaises(SyntaxError, timeit.Timer, stmt='return')
    TestTimeit.assertRaises(SyntaxError, timeit.Timer, stmt='yield')
    TestTimeit.assertRaises(SyntaxError, timeit.Timer, stmt='yield from ()')
    TestTimeit.assertRaises(SyntaxError, timeit.Timer, stmt='break')
    TestTimeit.assertRaises(SyntaxError, timeit.Timer, stmt='continue')
    TestTimeit.assertRaises(SyntaxError, timeit.Timer, stmt='from timeit import *')
    TestTimeit.assertRaises(SyntaxError, timeit.Timer, stmt='  pass')
    TestTimeit.assertRaises(SyntaxError, timeit.Timer, setup='while False:\n  pass', stmt='  break')

TestTimeit = test_timeit.TestTimeit()
test_timer_invalid_stmt()
