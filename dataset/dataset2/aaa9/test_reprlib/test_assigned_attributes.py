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

def test_assigned_attributes():
    from functools import WRAPPER_ASSIGNMENTS as assigned
    wrapped = test_reprlib.MyContainer3.wrapped
    wrapper = test_reprlib.MyContainer3.wrapper
    for name in assigned:
        TestRecursiveRepr.assertIs(getattr(wrapper, name), getattr(wrapped, name))

TestRecursiveRepr = test_reprlib.TestRecursiveRepr()
test_assigned_attributes()
