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

@unittest.skip('enable this test when working on pystate.c')
def test_unique_id():
    seen = set()
    for _ in range(100):
        id = test__xxsubinterpreters.interpreters.create()
        test__xxsubinterpreters.interpreters.destroy(id)
        seen.add(id)
    CreateTests.assertEqual(len(seen), 100)

CreateTests = test__xxsubinterpreters.CreateTests()
test_unique_id()
