from itertools import chain
import graphlib
import os
import unittest
from test.support.script_helper import assert_python_ok
import test_graphlib

def test_the_node_multiple_times():
    TestTopologicalSort._test_graph({1: {2}, 3: {4}, 0: [2, 4, 4, 4, 4, 4]}, [(2, 4), (1, 3, 0)])
    ts = graphlib.TopologicalSorter()
    ts.add(1, 2)
    ts.add(1, 2)
    ts.add(1, 2)
    TestTopologicalSort.assertEqual([*ts.static_order()], [2, 1])

TestTopologicalSort = test_graphlib.TestTopologicalSort()
test_the_node_multiple_times()
