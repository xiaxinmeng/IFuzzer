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

def test_bytes():
    ShareableTypeTests._assert_values((i.to_bytes(2, 'little', signed=True) for i in range(-1, 258)))

ShareableTypeTests = test__xxsubinterpreters.ShareableTypeTests()
ShareableTypeTests.setUp()
test_bytes()
