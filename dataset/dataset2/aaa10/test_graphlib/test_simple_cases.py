from itertools import chain
import graphlib
import os
import unittest
from test.support.script_helper import assert_python_ok
import test_graphlib

def test_simple_cases():
    TestTopologicalSort._test_graph({2: {11}, 9: {11, 8}, 10: {11, 3}, 11: {7, 5}, 8: {7, 3}}, [(3, 5, 7), (11, 8), (2, 10, 9)])
    TestTopologicalSort._test_graph({1: {}}, [(1,)])
    TestTopologicalSort._test_graph({x: {x + 1} for x in range(10)}, [(x,) for x in range(10, -1, -1)])
    TestTopologicalSort._test_graph({2: {3}, 3: {4}, 4: {5}, 5: {1}, 11: {12}, 12: {13}, 13: {14}, 14: {15}}, [(1, 15), (5, 14), (4, 13), (3, 12), (2, 11)])
    TestTopologicalSort._test_graph({0: [1, 2], 1: [3], 2: [5, 6], 3: [4], 4: [9], 5: [3], 6: [7], 7: [8], 8: [4], 9: []}, [(9,), (4,), (3, 8), (1, 5, 7), (6,), (2,), (0,)])
    TestTopologicalSort._test_graph({0: [1, 2], 1: [], 2: [3], 3: []}, [(1, 3), (2,), (0,)])
    TestTopologicalSort._test_graph({0: [1, 2], 1: [], 2: [3], 3: [], 4: [5], 5: [6], 6: []}, [(1, 3, 6), (2, 5), (0, 4)])

TestTopologicalSort = test_graphlib.TestTopologicalSort()
test_simple_cases()
