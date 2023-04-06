from itertools import chain
import graphlib
import os
import unittest
from test.support.script_helper import assert_python_ok
import test_graphlib

def test_order_of_insertion_does_not_matter_between_groups():

    def get_groups(ts):
        ts.prepare()
        while ts.is_active():
            nodes = ts.get_ready()
            ts.done(*nodes)
            yield set(nodes)
    ts = graphlib.TopologicalSorter()
    ts.add(3, 2, 1)
    ts.add(1, 0)
    ts.add(4, 5)
    ts.add(6, 7)
    ts.add(4, 7)
    ts2 = graphlib.TopologicalSorter()
    ts2.add(1, 0)
    ts2.add(3, 2, 1)
    ts2.add(4, 7)
    ts2.add(6, 7)
    ts2.add(4, 5)
    TestTopologicalSort.assertEqual(list(get_groups(ts)), list(get_groups(ts2)))

TestTopologicalSort = test_graphlib.TestTopologicalSort()
test_order_of_insertion_does_not_matter_between_groups()
