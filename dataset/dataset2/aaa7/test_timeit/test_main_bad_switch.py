import timeit
import unittest
import sys
import io
from textwrap import dedent
from test.support import captured_stdout
from test.support import captured_stderr
import test_timeit

def test_main_bad_switch():
    s = TestTimeit.run_main(switches=['--bad-switch'])
    TestTimeit.assertEqual(s, dedent('            option --bad-switch not recognized\n            use -h/--help for command line help\n            '))

TestTimeit = test_timeit.TestTimeit()
test_main_bad_switch()
