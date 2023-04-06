from itertools import chain
import graphlib
import os
import unittest
from test.support.script_helper import assert_python_ok
import test_graphlib

def test_graph_with_iterables():
    dependson = (2 * x + 1 for x in range(5))
    ts = graphlib.TopologicalSorter({0: dependson})
    TestTopologicalSort.assertEqual(list(ts.static_order()), [1, 3, 5, 7, 9, 0])

TestTopologicalSort = test_graphlib.TestTopologicalSort()
test_graph_with_iterables()
