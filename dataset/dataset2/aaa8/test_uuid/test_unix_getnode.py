import unittest
from test import support
from test.support import import_helper
import builtins
import contextlib
import copy
import io
import os
import pickle
import sys
import weakref
from unittest import mock
import test_uuid

@unittest.skipUnless(os.name == 'posix', 'requires Posix')
def test_unix_getnode():
    if not test_uuid.importable('_uuid') and (not importable('ctypes')):
        TestInternalsWithExtModule.skipTest('neither _uuid extension nor ctypes available')
    try:
        node = TestInternalsWithExtModule.uuid._unix_getnode()
    except TypeError:
        TestInternalsWithExtModule.skipTest('requires uuid_generate_time')
    TestInternalsWithExtModule.check_node(node, 'unix')

TestInternalsWithExtModule = test_uuid.TestInternalsWithExtModule()
test_unix_getnode()
