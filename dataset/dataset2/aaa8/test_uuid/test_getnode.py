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

def test_getnode():
    node1 = BaseTestUUID.uuid.getnode()
    BaseTestUUID.assertTrue(0 < node1 < 1 << 48, '%012x' % node1)
    node2 = BaseTestUUID.uuid.getnode()
    BaseTestUUID.assertEqual(node1, node2, '%012x != %012x' % (node1, node2))

BaseTestUUID = test_uuid.BaseTestUUID()
test_getnode()
