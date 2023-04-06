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

def test_down():
    StateTestCase.expect_set = [('line', 2, 'tfunc_main'), ('down',)]
    with test_bdb.TracerRun(StateTestCase) as tracer:
        StateTestCase.assertRaises(BdbError, tracer.runcall, tfunc_main)

StateTestCase = test_bdb.StateTestCase()
test_down()
