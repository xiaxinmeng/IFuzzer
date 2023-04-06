from itertools import chain
import graphlib
import os
import unittest
from test.support.script_helper import assert_python_ok
import test_graphlib

def test_is_active():
    ts = graphlib.TopologicalSorter()
    ts.add(1, 2)
    ts.prepare()
    TestTopologicalSort.assertTrue(ts.is_active())
    TestTopologicalSort.assertEqual(ts.get_ready(), (2,))
    TestTopologicalSort.assertTrue(ts.is_active())
    ts.done(2)
    TestTopologicalSort.assertTrue(ts.is_active())
    TestTopologicalSort.assertEqual(ts.get_ready(), (1,))
    TestTopologicalSort.assertTrue(ts.is_active())
    ts.done(1)
    TestTopologicalSort.assertFalse(ts.is_active())

TestTopologicalSort = test_graphlib.TestTopologicalSort()
test_is_active()
