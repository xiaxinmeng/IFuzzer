from itertools import chain
import graphlib
import os
import unittest
from test.support.script_helper import assert_python_ok
import test_graphlib

def test_invalid_nodes_in_done():
    ts = graphlib.TopologicalSorter()
    ts.add(1, 2, 3, 4)
    ts.add(2, 3, 4)
    ts.prepare()
    ts.get_ready()
    with TestTopologicalSort.assertRaisesRegex(ValueError, 'node 2 was not passed out'):
        ts.done(2)
    with TestTopologicalSort.assertRaisesRegex(ValueError, 'node 24 was not added using add\\(\\)'):
        ts.done(24)

TestTopologicalSort = test_graphlib.TestTopologicalSort()
test_invalid_nodes_in_done()
