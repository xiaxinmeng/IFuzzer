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

def test_strs():
    ShareableTypeTests._assert_values(['hello world', '你好世界', ''])

ShareableTypeTests = test__xxsubinterpreters.ShareableTypeTests()
ShareableTypeTests.setUp()
test_strs()
