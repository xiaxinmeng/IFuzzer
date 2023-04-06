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

@contextmanager
def test_issue29692():
    try:
        yield
    except Exception as exc:
        raise RuntimeError('issue29692:Chained') from exc

ContextManagerTestCase = test_contextlib.ContextManagerTestCase()
test_issue29692()
