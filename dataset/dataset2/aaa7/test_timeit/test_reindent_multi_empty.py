import timeit
import unittest
import sys
import io
from textwrap import dedent
from test.support import captured_stdout
from test.support import captured_stderr
import test_timeit

def test_reindent_multi_empty():
    TestTimeit.assertEqual(timeit.reindent('\n\n', 0), '\n\n')
    TestTimeit.assertEqual(timeit.reindent('\n\n', 4), '\n    \n    ')

TestTimeit = test_timeit.TestTimeit()
test_reindent_multi_empty()
