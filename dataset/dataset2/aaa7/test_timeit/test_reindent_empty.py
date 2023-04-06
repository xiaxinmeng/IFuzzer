import timeit
import unittest
import sys
import io
from textwrap import dedent
from test.support import captured_stdout
from test.support import captured_stderr
import test_timeit

def test_reindent_empty():
    TestTimeit.assertEqual(timeit.reindent('', 0), '')
    TestTimeit.assertEqual(timeit.reindent('', 4), '')

TestTimeit = test_timeit.TestTimeit()
test_reindent_empty()
