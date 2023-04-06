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

def test_one():
    id1 = test__xxsubinterpreters.interpreters.create()
    id2 = test__xxsubinterpreters.interpreters.create()
    id3 = test__xxsubinterpreters.interpreters.create()
    DestroyTests.assertIn(id2, test__xxsubinterpreters.interpreters.list_all())
    test__xxsubinterpreters.interpreters.destroy(id2)
    DestroyTests.assertNotIn(id2, test__xxsubinterpreters.interpreters.list_all())
    DestroyTests.assertIn(id1, test__xxsubinterpreters.interpreters.list_all())
    DestroyTests.assertIn(id3, test__xxsubinterpreters.interpreters.list_all())

DestroyTests = test__xxsubinterpreters.DestroyTests()
test_one()
