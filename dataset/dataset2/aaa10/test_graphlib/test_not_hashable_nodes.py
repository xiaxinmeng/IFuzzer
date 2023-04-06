from itertools import chain
import graphlib
import os
import unittest
from test.support.script_helper import assert_python_ok
import test_graphlib

def test_not_hashable_nodes():
    ts = graphlib.TopologicalSorter()
    TestTopologicalSort.assertRaises(TypeError, ts.add, dict(), 1)
    TestTopologicalSort.assertRaises(TypeError, ts.add, 1, dict())
    TestTopologicalSort.assertRaises(TypeError, ts.add, dict(), dict())

TestTopologicalSort = test_graphlib.TestTopologicalSort()
test_not_hashable_nodes()
