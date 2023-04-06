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

def test_from_other_thread():
    id = test__xxsubinterpreters.interpreters.create()

    def f():
        test__xxsubinterpreters.interpreters.destroy(id)
    t = threading.Thread(target=f)
    t.start()
    t.join()

DestroyTests = test__xxsubinterpreters.DestroyTests()
test_from_other_thread()
