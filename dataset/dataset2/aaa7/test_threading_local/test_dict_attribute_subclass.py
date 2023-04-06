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

def test_dict_attribute_subclass():

    class LocalSubclass(BaseLocalTest._local):
        """To test that subclasses behave properly."""
    BaseLocalTest._test_dict_attribute(LocalSubclass)

BaseLocalTest = test_threading_local.BaseLocalTest()
test_dict_attribute_subclass()
