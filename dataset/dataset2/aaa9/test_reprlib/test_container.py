import sys
import os
import shutil
import importlib
import importlib.util
import unittest
from test.support import verbose
from test.support.os_helper import create_empty_file
from reprlib import repr as r
from reprlib import Repr
from reprlib import recursive_repr
from array import array
from collections import deque

from functools import WRAPPER_ASSIGNMENTS as assigned
import test_reprlib

def test_container():
    from array import array
    from collections import deque
    eq = ReprTests.assertEqual
    eq(r(()), '()')
    eq(r((1,)), '(1,)')
    eq(r((1, 2, 3)), '(1, 2, 3)')
    eq(r((1, 2, 3, 4, 5, 6)), '(1, 2, 3, 4, 5, 6)')
    eq(r((1, 2, 3, 4, 5, 6, 7)), '(1, 2, 3, 4, 5, 6, ...)')
    eq(r([]), '[]')
    eq(r([1]), '[1]')
    eq(r([1, 2, 3]), '[1, 2, 3]')
    eq(r([1, 2, 3, 4, 5, 6]), '[1, 2, 3, 4, 5, 6]')
    eq(r([1, 2, 3, 4, 5, 6, 7]), '[1, 2, 3, 4, 5, 6, ...]')
    eq(r(set([])), 'set()')
    eq(r(set([1])), '{1}')
    eq(r(set([1, 2, 3])), '{1, 2, 3}')
    eq(r(set([1, 2, 3, 4, 5, 6])), '{1, 2, 3, 4, 5, 6}')
    eq(r(set([1, 2, 3, 4, 5, 6, 7])), '{1, 2, 3, 4, 5, 6, ...}')
    eq(r(frozenset([])), 'frozenset()')
    eq(r(frozenset([1])), 'frozenset({1})')
    eq(r(frozenset([1, 2, 3])), 'frozenset({1, 2, 3})')
    eq(r(frozenset([1, 2, 3, 4, 5, 6])), 'frozenset({1, 2, 3, 4, 5, 6})')
    eq(r(frozenset([1, 2, 3, 4, 5, 6, 7])), 'frozenset({1, 2, 3, 4, 5, 6, ...})')
    eq(r(deque([1, 2, 3, 4, 5, 6, 7])), 'deque([1, 2, 3, 4, 5, 6, ...])')
    eq(r({}), '{}')
    d = {'alice': 1, 'bob': 2, 'charles': 3, 'dave': 4}
    eq(r(d), "{'alice': 1, 'bob': 2, 'charles': 3, 'dave': 4}")
    d['arthur'] = 1
    eq(r(d), "{'alice': 1, 'arthur': 1, 'bob': 2, 'charles': 3, ...}")
    eq(r(array('i')), "array('i')")
    eq(r(array('i', [1])), "array('i', [1])")
    eq(r(array('i', [1, 2])), "array('i', [1, 2])")
    eq(r(array('i', [1, 2, 3])), "array('i', [1, 2, 3])")
    eq(r(array('i', [1, 2, 3, 4])), "array('i', [1, 2, 3, 4])")
    eq(r(array('i', [1, 2, 3, 4, 5])), "array('i', [1, 2, 3, 4, 5])")
    eq(r(array('i', [1, 2, 3, 4, 5, 6])), "array('i', [1, 2, 3, 4, 5, ...])")

ReprTests = test_reprlib.ReprTests()
test_container()
