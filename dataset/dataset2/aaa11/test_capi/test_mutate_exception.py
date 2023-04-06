from collections import OrderedDict
import os
import pickle
import random
import re
import subprocess
import sys
import textwrap
import threading
import time
import unittest
import weakref
import importlib.machinery
import importlib.util
from test import support
from test.support import MISSING_C_DOCSTRINGS
from test.support import import_helper
from test.support import threading_helper
from test.support import warnings_helper
from test.support.script_helper import assert_python_failure, assert_python_ok
import _posixsubprocess
import _testinternalcapi
from _testcapi import MyList
from _testcapi import MyList
from _testcapi import pynumber_tobase
import builtins
import binascii
import test_capi

def test_mutate_exception():
    """
        Exceptions saved in global module state get shared between
        individual module instances. This test checks whether or not
        a change in one interpreter's module gets reflected into the
        other ones.
        """
    import binascii
    support.run_in_subinterp("import binascii; binascii.Error.foobar = 'foobar'")
    SubinterpreterTest.assertFalse(hasattr(binascii.Error, 'foobar'))

SubinterpreterTest = test_capi.SubinterpreterTest()
test_mutate_exception()
