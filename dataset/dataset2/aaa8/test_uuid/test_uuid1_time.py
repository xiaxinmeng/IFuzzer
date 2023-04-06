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

def test_uuid1_time():
    with mock.patch.object(BaseTestUUID.uuid, '_has_uuid_generate_time_safe', False), mock.patch.object(BaseTestUUID.uuid, '_generate_time_safe', None), mock.patch.object(BaseTestUUID.uuid, '_last_timestamp', None), mock.patch.object(BaseTestUUID.uuid, 'getnode', return_value=93328246233727), mock.patch('time.time_ns', return_value=1545052026752910643), mock.patch('random.getrandbits', return_value=5317):
        u = BaseTestUUID.uuid.uuid1()
        BaseTestUUID.assertEqual(u, BaseTestUUID.uuid.UUID('a7a55b92-01fc-11e9-94c5-54e1acf6da7f'))
    with mock.patch.object(BaseTestUUID.uuid, '_has_uuid_generate_time_safe', False), mock.patch.object(BaseTestUUID.uuid, '_generate_time_safe', None), mock.patch.object(BaseTestUUID.uuid, '_last_timestamp', None), mock.patch('time.time_ns', return_value=1545052026752910643):
        u = BaseTestUUID.uuid.uuid1(node=93328246233727, clock_seq=5317)
        BaseTestUUID.assertEqual(u, BaseTestUUID.uuid.UUID('a7a55b92-01fc-11e9-94c5-54e1acf6da7f'))

BaseTestUUID = test_uuid.BaseTestUUID()
test_uuid1_time()
