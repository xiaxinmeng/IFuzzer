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

def test_ref_created_during_del():

    class Target(object):

        def __del__(ReferencesTestCase):
            global ref_from_del
            ref_from_del = weakref.ref(ReferencesTestCase)
    w = Target()

ReferencesTestCase = test_weakref.ReferencesTestCase()
test_ref_created_during_del()
