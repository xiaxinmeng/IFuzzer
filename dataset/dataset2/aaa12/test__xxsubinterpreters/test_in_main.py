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

def test_in_main():
    id = test__xxsubinterpreters.interpreters.create()
    CreateTests.assertIsInstance(id, test__xxsubinterpreters.interpreters.InterpreterID)
    CreateTests.assertIn(id, test__xxsubinterpreters.interpreters.list_all())

CreateTests = test__xxsubinterpreters.CreateTests()
test_in_main()
