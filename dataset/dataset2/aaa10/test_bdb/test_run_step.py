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

def test_run_step():
    code = '\n            lno = 2\n        '
    RunTestCase.expect_set = [('line', 2, '<module>'), ('step',), ('return', 2, '<module>'), ('quit',)]
    with test_bdb.TracerRun(RunTestCase) as tracer:
        tracer.run(compile(textwrap.dedent(code), '<string>', 'exec'))

RunTestCase = test_bdb.RunTestCase()
test_run_step()
