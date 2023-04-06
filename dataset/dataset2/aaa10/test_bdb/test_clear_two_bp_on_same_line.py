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

def test_clear_two_bp_on_same_line():
    code = '\n            def func():\n                lno = 3\n                lno = 4\n\n            def main():\n                for i in range(3):\n                    func()\n        '
    modules = {test_bdb.TEST_MODULE: code}
    with test_bdb.create_modules(modules):
        BreakpointTestCase.expect_set = [('line', 2, 'tfunc_import'), ('break', (test_bdb.TEST_MODULE_FNAME, 3)), ('None', 2, 'tfunc_import'), ('break', (test_bdb.TEST_MODULE_FNAME, 3)), ('None', 2, 'tfunc_import'), ('break', (test_bdb.TEST_MODULE_FNAME, 4)), ('None', 2, 'tfunc_import'), ('continue',), ('line', 3, 'func', ({1: 1}, [])), ('continue',), ('line', 4, 'func', ({3: 1}, [])), ('clear', (test_bdb.TEST_MODULE_FNAME, 3)), ('None', 4, 'func'), ('continue',), ('line', 4, 'func', ({3: 2}, [])), ('quit',)]
        with test_bdb.TracerRun(BreakpointTestCase) as tracer:
            tracer.runcall(tfunc_import)

BreakpointTestCase = test_bdb.BreakpointTestCase()
test_clear_two_bp_on_same_line()
