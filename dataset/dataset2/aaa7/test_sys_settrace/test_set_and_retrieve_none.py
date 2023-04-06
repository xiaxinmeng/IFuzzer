from test import support
import unittest
import sys
import difflib
import gc
from functools import wraps
import asyncio
import gc
import test_sys_settrace

def test_set_and_retrieve_none():
    sys.settrace(None)
    assert sys.gettrace() is None

TraceTestCase = test_sys_settrace.TraceTestCase()
test_set_and_retrieve_none()
