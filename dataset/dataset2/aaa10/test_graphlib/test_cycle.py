from itertools import chain
import graphlib
import os
import unittest
from test.support.script_helper import assert_python_ok
import test_graphlib

def test_cycle():
    TestTopologicalSort._assert_cycle({1: {1}}, [1, 1])
    TestTopologicalSort._assert_cycle({1: {2}, 2: {1}}, [1, 2, 1])
    TestTopologicalSort._assert_cycle({1: {2}, 2: {3}, 3: {1}}, [1, 3, 2, 1])
    TestTopologicalSort._assert_cycle({1: {2}, 2: {3}, 3: {1}, 5: {4}, 4: {6}}, [1, 3, 2, 1])
    TestTopologicalSort._assert_cycle({1: {2}, 2: {1}, 3: {4}, 4: {5}, 6: {7}, 7: {6}}, [1, 2, 1])
    TestTopologicalSort._assert_cycle({1: {2}, 2: {3}, 3: {2, 4}, 4: {5}}, [3, 2])

TestTopologicalSort = test_graphlib.TestTopologicalSort()
test_cycle()
