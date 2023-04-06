from itertools import chain
import graphlib
import os
import unittest
from test.support.script_helper import assert_python_ok
import test_graphlib

def test_done():
    ts = graphlib.TopologicalSorter()
    ts.add(1, 2, 3, 4)
    ts.add(2, 3)
    ts.prepare()
    TestTopologicalSort.assertEqual(ts.get_ready(), (3, 4))
    TestTopologicalSort.assertEqual(ts.get_ready(), ())
    ts.done(3)
    TestTopologicalSort.assertEqual(ts.get_ready(), (2,))
    TestTopologicalSort.assertEqual(ts.get_ready(), ())
    ts.done(4)
    ts.done(2)
    TestTopologicalSort.assertEqual(ts.get_ready(), (1,))
    TestTopologicalSort.assertEqual(ts.get_ready(), ())
    ts.done(1)
    TestTopologicalSort.assertEqual(ts.get_ready(), ())
    TestTopologicalSort.assertFalse(ts.is_active())

TestTopologicalSort = test_graphlib.TestTopologicalSort()
test_done()
