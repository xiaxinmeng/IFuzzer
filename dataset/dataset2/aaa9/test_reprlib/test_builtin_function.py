import sys
import os
import shutil
import importlib
import importlib.util
import unittest
from test.support import verbose
from test.support.os_helper import create_empty_file
from reprlib import repr as r
from reprlib import Repr
from reprlib import recursive_repr
from array import array
from collections import deque

from functools import WRAPPER_ASSIGNMENTS as assigned
import test_reprlib

@unittest.skip('needs a built-in function with a really long name')
def test_builtin_function():
    pass

ReprTests = test_reprlib.ReprTests()
test_builtin_function()
