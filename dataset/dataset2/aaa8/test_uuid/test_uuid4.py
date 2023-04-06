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

def test_uuid4():
    equal = BaseTestUUID.assertEqual
    for u in [BaseTestUUID.uuid.uuid4() for i in range(10)]:
        equal(u.variant, BaseTestUUID.uuid.RFC_4122)
        equal(u.version, 4)
    uuids = {}
    for u in [BaseTestUUID.uuid.uuid4() for i in range(1000)]:
        uuids[u] = 1
    equal(len(uuids.keys()), 1000)

BaseTestUUID = test_uuid.BaseTestUUID()
test_uuid4()
