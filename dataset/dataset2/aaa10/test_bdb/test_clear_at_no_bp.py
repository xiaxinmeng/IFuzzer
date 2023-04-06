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

def test_clear_at_no_bp():
    BreakpointTestCase.expect_set = [('line', 2, 'tfunc_import'), ('clear', (__file__, 1))]
    with test_bdb.TracerRun(BreakpointTestCase) as tracer:
        BreakpointTestCase.assertRaises(BdbError, tracer.runcall, tfunc_import)

BreakpointTestCase = test_bdb.BreakpointTestCase()
test_clear_at_no_bp()
