import timeit
import unittest
import sys
import io
from textwrap import dedent
from test.support import captured_stdout
from test.support import captured_stderr
import test_timeit

def test_timer_invalid_setup():
    TestTimeit.assertRaises(ValueError, timeit.Timer, setup=None)
    TestTimeit.assertRaises(SyntaxError, timeit.Timer, setup='return')
    TestTimeit.assertRaises(SyntaxError, timeit.Timer, setup='yield')
    TestTimeit.assertRaises(SyntaxError, timeit.Timer, setup='yield from ()')
    TestTimeit.assertRaises(SyntaxError, timeit.Timer, setup='break')
    TestTimeit.assertRaises(SyntaxError, timeit.Timer, setup='continue')
    TestTimeit.assertRaises(SyntaxError, timeit.Timer, setup='from timeit import *')
    TestTimeit.assertRaises(SyntaxError, timeit.Timer, setup='  pass')

TestTimeit = test_timeit.TestTimeit()
test_timer_invalid_setup()
