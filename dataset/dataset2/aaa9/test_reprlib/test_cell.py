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

def test_cell():

    def get_cell():
        x = 42

        def inner():
            return x
        return inner
    x = get_cell().__closure__[0]
    ReprTests.assertRegex(repr(x), '<cell at 0x[0-9A-Fa-f]+: int object at 0x[0-9A-Fa-f]+>')
    ReprTests.assertRegex(r(x), '<cell at 0x.*\\.\\.\\..*>')

ReprTests = test_reprlib.ReprTests()
test_cell()
