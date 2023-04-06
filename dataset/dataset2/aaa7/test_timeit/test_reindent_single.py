import timeit
import unittest
import sys
import io
from textwrap import dedent
from test.support import captured_stdout
from test.support import captured_stderr
import test_timeit

def test_reindent_single():
    TestTimeit.assertEqual(timeit.reindent('pass', 0), 'pass')
    TestTimeit.assertEqual(timeit.reindent('pass', 4), 'pass')

TestTimeit = test_timeit.TestTimeit()
test_reindent_single()
