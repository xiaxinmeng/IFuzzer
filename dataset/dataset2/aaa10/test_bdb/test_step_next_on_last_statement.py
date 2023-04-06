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

def test_step_next_on_last_statement():
    for set_type in ('step', 'next'):
        with StateTestCase.subTest(set_type=set_type):
            StateTestCase.expect_set = [('line', 2, 'tfunc_main'), ('step',), ('line', 3, 'tfunc_main'), ('step',), ('call', 1, 'tfunc_first'), ('break', (__file__, 3)), ('None', 1, 'tfunc_first'), ('continue',), ('line', 3, 'tfunc_first', ({1: 1}, [])), (set_type,), ('line', 4, 'tfunc_first'), ('quit',)]
            with test_bdb.TracerRun(StateTestCase) as tracer:
                tracer.runcall(tfunc_main)

StateTestCase = test_bdb.StateTestCase()
test_step_next_on_last_statement()
