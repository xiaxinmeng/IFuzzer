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

def test_from_main():
    [expected] = test__xxsubinterpreters.interpreters.list_all()
    main = test__xxsubinterpreters.interpreters.get_main()
    GetMainTests.assertEqual(main, expected)
    GetMainTests.assertIsInstance(main, test__xxsubinterpreters.interpreters.InterpreterID)

GetMainTests = test__xxsubinterpreters.GetMainTests()
test_from_main()
