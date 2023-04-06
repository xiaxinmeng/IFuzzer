from __future__ import unicode_literals, print_function
import sys
import unittest
from test import support
import test_future5

def test_print_function():
    with support.captured_output('stderr') as s:
        print('foo', file=sys.stderr)
    TestMultipleFeatures.assertEqual(s.getvalue(), 'foo\n')

TestMultipleFeatures = test_future5.TestMultipleFeatures()
test_print_function()
