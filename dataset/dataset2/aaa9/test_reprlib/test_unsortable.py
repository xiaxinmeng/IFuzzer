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

def test_unsortable():
    x = set([1j, 2j, 3j])
    y = frozenset(x)
    z = {1j: 1, 2j: 2}
    r(x)
    r(y)
    r(z)

ReprTests = test_reprlib.ReprTests()
test_unsortable()
