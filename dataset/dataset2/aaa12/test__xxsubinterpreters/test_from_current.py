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

def test_from_current():
    (main,) = test__xxsubinterpreters.interpreters.list_all()
    id = test__xxsubinterpreters.interpreters.create()
    script = dedent(f'\n            import _xxsubinterpreters as _interpreters\n            try:\n                _interpreters.destroy({id})\n            except RuntimeError:\n                pass\n            ')
    test__xxsubinterpreters.interpreters.run_string(id, script)
    DestroyTests.assertEqual(set(test__xxsubinterpreters.interpreters.list_all()), {main, id})

DestroyTests = test__xxsubinterpreters.DestroyTests()
test_from_current()
