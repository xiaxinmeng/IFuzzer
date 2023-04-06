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

def test_runeval_step():
    code = '\n            def main():\n                lno = 3\n        '
    modules = {test_bdb.TEST_MODULE: code}
    with test_bdb.create_modules(modules):
        RunTestCase.expect_set = [('line', 1, '<module>'), ('step',), ('call', 2, 'main'), ('step',), ('line', 3, 'main'), ('step',), ('return', 3, 'main'), ('step',), ('return', 1, '<module>'), ('quit',)]
        import test_module_for_bdb
        with test_bdb.TracerRun(RunTestCase) as tracer:
            tracer.runeval('test_module_for_bdb.main()', globals(), locals())

RunTestCase = test_bdb.RunTestCase()
test_runeval_step()
