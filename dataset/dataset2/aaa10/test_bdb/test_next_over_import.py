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

def test_next_over_import():
    code = '\n            def main():\n                lno = 3\n        '
    modules = {test_bdb.TEST_MODULE: code}
    with test_bdb.create_modules(modules):
        StateTestCase.expect_set = [('line', 2, 'tfunc_import'), ('next',), ('line', 3, 'tfunc_import'), ('quit',)]
        with test_bdb.TracerRun(StateTestCase) as tracer:
            tracer.runcall(tfunc_import)

StateTestCase = test_bdb.StateTestCase()
test_next_over_import()
