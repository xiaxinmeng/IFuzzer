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

def test_types():
    ShareableTypeTests._assert_values([b'spam', 9999, ShareableTypeTests.cid])

ShareableTypeTests = test__xxsubinterpreters.ShareableTypeTests()
ShareableTypeTests.setUp()
test_types()
