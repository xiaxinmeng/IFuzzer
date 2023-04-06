from itertools import chain
import graphlib
import os
import unittest
from test.support.script_helper import assert_python_ok
import test_graphlib

def test_prepare_multiple_times():
    ts = graphlib.TopologicalSorter()
    ts.prepare()
    with TestTopologicalSort.assertRaisesRegex(ValueError, 'cannot prepare\\(\\) more than once'):
        ts.prepare()

TestTopologicalSort = test_graphlib.TestTopologicalSort()
test_prepare_multiple_times()
