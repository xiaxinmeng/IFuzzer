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

def test_arguments():

    class MyLocal(BaseLocalTest._local):

        def __init__(BaseLocalTest, *args, **kwargs):
            pass
    MyLocal(a=1)
    MyLocal(1)
    BaseLocalTest.assertRaises(TypeError, BaseLocalTest._local, a=1)
    BaseLocalTest.assertRaises(TypeError, BaseLocalTest._local, 1)

BaseLocalTest = test_threading_local.BaseLocalTest()

test_arguments()
