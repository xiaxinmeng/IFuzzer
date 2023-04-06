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

def test_return():
    StateTestCase.expect_set = [('line', 2, 'tfunc_main'), ('step',), ('line', 3, 'tfunc_main'), ('step',), ('call', 1, 'tfunc_first'), ('step',), ('line', 2, 'tfunc_first'), ('return',), ('return', 4, 'tfunc_first'), ('step',), ('line', 4, 'tfunc_main'), ('quit',)]
    with test_bdb.TracerRun(StateTestCase) as tracer:
        tracer.runcall(tfunc_main)

StateTestCase = test_bdb.StateTestCase()
test_return()
