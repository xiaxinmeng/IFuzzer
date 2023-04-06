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

def test_ignore_count_on_disabled_bp():
    code = '\n            def func():\n                lno = 3\n\n            def main():\n                for i in range(3):\n                    func()\n        '
    modules = {test_bdb.TEST_MODULE: code}
    with test_bdb.create_modules(modules):
        BreakpointTestCase.expect_set = [('line', 2, 'tfunc_import'), test_bdb.break_in_func('func', test_bdb.TEST_MODULE_FNAME), ('None', 2, 'tfunc_import'), test_bdb.break_in_func('func', test_bdb.TEST_MODULE_FNAME), ('None', 2, 'tfunc_import'), ('ignore', (1,)), ('None', 2, 'tfunc_import'), ('disable', (1,)), ('None', 2, 'tfunc_import'), ('continue',), ('line', 3, 'func', ({2: 1}, [])), ('enable', (1,)), ('None', 3, 'func'), ('continue',), ('line', 3, 'func', ({2: 2}, [])), ('continue',), ('line', 3, 'func', ({1: 2}, [])), ('quit',)]
        with test_bdb.TracerRun(BreakpointTestCase) as tracer:
            tracer.runcall(tfunc_import)

BreakpointTestCase = test_bdb.BreakpointTestCase()
test_ignore_count_on_disabled_bp()
