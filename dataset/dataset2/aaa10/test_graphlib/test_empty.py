from itertools import chain
import graphlib
import os
import unittest
from test.support.script_helper import assert_python_ok
import test_graphlib

def test_empty():
    TestTopologicalSort._test_graph({}, [])

TestTopologicalSort = test_graphlib.TestTopologicalSort()
test_empty()
