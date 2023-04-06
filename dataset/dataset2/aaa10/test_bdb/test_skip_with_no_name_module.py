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

def test_skip_with_no_name_module():
    bdb = test_bdb.Bdb(skip=['anything*'])
    StateTestCase.assertIs(bdb.is_skipped_module(None), False)

StateTestCase = test_bdb.StateTestCase()
test_skip_with_no_name_module()
