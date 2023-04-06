import bdb as _bdb
import sys
import os
import unittest
import textwrap
import importlib
import linecache
from contextlib import contextmanager
from itertools import islice, repeat
import test.support
from test.support import import_helper
from test.support import os_helper
import test_bdb

def test_until_with_too_large_count():
    StateTestCase.expect_set = [('line', 2, 'tfunc_main'), test_bdb.break_in_func('tfunc_first'), ('None', 2, 'tfunc_main'), ('continue',), ('line', 2, 'tfunc_first', ({1: 1}, [])), ('until', (9999,)), ('return', 4, 'tfunc_first'), ('quit',)]
    with test_bdb.TracerRun(StateTestCase) as tracer:
        tracer.runcall(tfunc_main)

StateTestCase = test_bdb.StateTestCase()
test_until_with_too_large_count()
