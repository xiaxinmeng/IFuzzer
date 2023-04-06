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

def test_uuid1_eui64():
    too_large_getter = lambda : 1 << 48
    with mock.patch.multiple(BaseTestUUID.uuid, _node=None, _GETTERS=[too_large_getter]):
        node = BaseTestUUID.uuid.getnode()
    BaseTestUUID.assertTrue(0 < node < 1 << 48, '%012x' % node)
    try:
        BaseTestUUID.uuid.uuid1(node=node)
    except ValueError:
        BaseTestUUID.fail('uuid1 was given an invalid node ID')

BaseTestUUID = test_uuid.BaseTestUUID()
test_uuid1_eui64()
