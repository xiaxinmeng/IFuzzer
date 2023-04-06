from itertools import chain
import graphlib
import os
import unittest
from test.support.script_helper import assert_python_ok
import test_graphlib

def test_calls_before_prepare():
    ts = graphlib.TopologicalSorter()
    with TestTopologicalSort.assertRaisesRegex(ValueError, 'prepare\\(\\) must be called first'):
        ts.get_ready()
    with TestTopologicalSort.assertRaisesRegex(ValueError, 'prepare\\(\\) must be called first'):
        ts.done(3)
    with TestTopologicalSort.assertRaisesRegex(ValueError, 'prepare\\(\\) must be called first'):
        ts.is_active()

TestTopologicalSort = test_graphlib.TestTopologicalSort()
test_calls_before_prepare()
