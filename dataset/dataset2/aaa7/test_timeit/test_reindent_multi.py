import timeit
import unittest
import sys
import io
from textwrap import dedent
from test.support import captured_stdout
from test.support import captured_stderr
import test_timeit

def test_reindent_multi():
    TestTimeit.assertEqual(timeit.reindent('print()\npass\nbreak', 0), 'print()\npass\nbreak')
    TestTimeit.assertEqual(timeit.reindent('print()\npass\nbreak', 4), 'print()\n    pass\n    break')

TestTimeit = test_timeit.TestTimeit()
test_reindent_multi()
