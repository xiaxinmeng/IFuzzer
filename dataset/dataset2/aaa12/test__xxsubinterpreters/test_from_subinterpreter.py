from collections import namedtuple
import contextlib
import itertools
import os
import pickle
import sys
from textwrap import dedent
import threading
import time
import unittest
from test import support
from test.support import import_helper
from test.support import script_helper
import tempfile
import test__xxsubinterpreters

def test_from_subinterpreter():
    interp = test__xxsubinterpreters.interpreters.create()
    out = test__xxsubinterpreters._run_output(interp, dedent(f'\n            import _xxsubinterpreters as _interpreters\n            if _interpreters.is_running({interp}):\n                print(True)\n            else:\n                print(False)\n            '))
    GetMainTests.assertEqual(out.strip(), 'True')

GetMainTests = test__xxsubinterpreters.GetMainTests()
test_from_subinterpreter()
