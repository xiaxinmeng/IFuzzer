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

@support.requires_mac_ver(10, 5)
@unittest.skipUnless(os.name == 'posix', 'POSIX-only test')
def test_uuid1_safe():
    if not BaseTestUUID.uuid._has_uuid_generate_time_safe:
        BaseTestUUID.skipTest('requires uuid_generate_time_safe(3)')
    u = BaseTestUUID.uuid.uuid1()
    BaseTestUUID.assertNotEqual(u.is_safe, BaseTestUUID.uuid.SafeUUID.unknown)

BaseTestUUID = test_uuid.BaseTestUUID()
test_uuid1_safe()
