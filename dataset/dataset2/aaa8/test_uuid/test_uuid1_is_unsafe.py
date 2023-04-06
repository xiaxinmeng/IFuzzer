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

@unittest.skipUnless(os.name == 'posix', 'POSIX-only test')
def test_uuid1_is_unsafe():
    with BaseTestUUID.mock_generate_time_safe(-1):
        u = BaseTestUUID.uuid.uuid1()
        BaseTestUUID.assertEqual(u.is_safe, BaseTestUUID.uuid.SafeUUID.unsafe)

BaseTestUUID = test_uuid.BaseTestUUID()
test_uuid1_is_unsafe()
