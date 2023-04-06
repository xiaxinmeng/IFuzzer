from itertools import chain
import graphlib
import os
import unittest
from test.support.script_helper import assert_python_ok
import test_graphlib

def test_add_dependencies_for_same_node_incrementally():
    ts = graphlib.TopologicalSorter()
    ts.add(1, 2)
    ts.add(1, 3)
    ts.add(1, 4)
    ts.add(1, 5)
    ts2 = graphlib.TopologicalSorter({1: {2, 3, 4, 5}})
    TestTopologicalSort.assertEqual([*ts.static_order()], [*ts2.static_order()])

TestTopologicalSort = test_graphlib.TestTopologicalSort()
test_add_dependencies_for_same_node_incrementally()
