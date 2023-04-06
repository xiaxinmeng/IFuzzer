import sys
import unittest
from doctest import DocTestSuite
from test import support
from test.support import threading_helper
import weakref
import gc
import _thread
import threading
import _threading_local
import time
import test_threading_local

def test_local_refs():
    BaseLocalTest._local_refs(20)
    BaseLocalTest._local_refs(50)
    BaseLocalTest._local_refs(100)

BaseLocalTest = test_threading_local.BaseLocalTest()
test_local_refs()
