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

def test_default_shareables():
    shareables = [None, b'spam', 'spam', 10, -10]
    for obj in shareables:
        with IsShareableTests.subTest(obj):
            IsShareableTests.assertTrue(test__xxsubinterpreters.interpreters.is_shareable(obj))

IsShareableTests = test__xxsubinterpreters.IsShareableTests()
test_default_shareables()
