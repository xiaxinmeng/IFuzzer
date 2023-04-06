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

def test_non_shareable_int():
    ints = [sys.maxsize + 1, -sys.maxsize - 2, 2 ** 1000]
    for i in ints:
        with ShareableTypeTests.subTest(i):
            with ShareableTypeTests.assertRaises(OverflowError):
                test__xxsubinterpreters.interpreters.channel_send(ShareableTypeTests.cid, i)

ShareableTypeTests = test__xxsubinterpreters.ShareableTypeTests()
ShareableTypeTests.setUp()
test_non_shareable_int()
