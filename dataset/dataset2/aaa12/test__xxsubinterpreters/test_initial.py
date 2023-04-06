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

def test_initial():
    main = test__xxsubinterpreters.interpreters.get_main()
    ids = test__xxsubinterpreters.interpreters.list_all()
    ListAllTests.assertEqual(ids, [main])

ListAllTests = test__xxsubinterpreters.ListAllTests()
test_initial()
