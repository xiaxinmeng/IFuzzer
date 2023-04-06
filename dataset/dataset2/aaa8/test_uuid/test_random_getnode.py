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

def test_random_getnode():
    node = BaseTestInternals.uuid._random_getnode()
    BaseTestInternals.assertTrue(node & 1 << 40, '%012x' % node)
    BaseTestInternals.check_node(node)
    node2 = BaseTestInternals.uuid._random_getnode()
    BaseTestInternals.assertNotEqual(node2, node, '%012x' % node)

BaseTestInternals = test_uuid.BaseTestInternals()
test_random_getnode()
