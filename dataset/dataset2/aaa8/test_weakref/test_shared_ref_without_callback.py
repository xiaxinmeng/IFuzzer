import gc
import sys
import unittest
import collections
import weakref
import operator
import contextlib
import copy
import threading
import time
import random
from test import support
from test.support import script_helper, ALWAYS_EQ
import _testcapi
import gc
import gc
import gc
import gc
import gc
import gc
import gc
from test import mapping_tests
import test_weakref

def test_shared_ref_without_callback():
    ReferencesTestCase.check_shared_without_callback(weakref.ref)

ReferencesTestCase = test_weakref.ReferencesTestCase()
test_shared_ref_without_callback()
