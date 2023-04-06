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

def test_bp_on_non_existent_module():
    BreakpointTestCase.expect_set = [('line', 2, 'tfunc_import'), ('break', ('/non/existent/module.py', 1))]
    with test_bdb.TracerRun(BreakpointTestCase) as tracer:
        BreakpointTestCase.assertRaises(BdbError, tracer.runcall, tfunc_import)

BreakpointTestCase = test_bdb.BreakpointTestCase()
test_bp_on_non_existent_module()
