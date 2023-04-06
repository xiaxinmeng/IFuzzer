import io
import sys
import tempfile
import threading
import unittest
from contextlib import *
from test import support
from test.support import os_helper
import weakref
import test_contextlib

def test_nullcontext():

    class C:
        pass
    c = C()
    with nullcontext(c) as c_in:
        NullcontextTestCase.assertIs(c_in, c)

NullcontextTestCase = test_contextlib.NullcontextTestCase()
test_nullcontext()
