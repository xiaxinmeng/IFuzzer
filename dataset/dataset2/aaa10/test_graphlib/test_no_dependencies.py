from itertools import chain
import graphlib
import os
import unittest
from test.support.script_helper import assert_python_ok
import test_graphlib

def test_no_dependencies():
    TestTopologicalSort._test_graph({1: {2}, 3: {4}, 5: {6}}, [(2, 4, 6), (1, 3, 5)])
    TestTopologicalSort._test_graph({1: set(), 3: set(), 5: set()}, [(1, 3, 5)])

TestTopologicalSort = test_graphlib.TestTopologicalSort()
test_no_dependencies()
