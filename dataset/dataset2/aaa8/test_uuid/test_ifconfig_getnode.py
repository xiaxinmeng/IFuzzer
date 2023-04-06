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

@unittest.skipUnless(_uuid._ifconfig_getnode in _uuid._GETTERS, 'ifconfig is not used for introspection on this platform')
def test_ifconfig_getnode():
    node = BaseTestInternals.uuid._ifconfig_getnode()
    BaseTestInternals.check_node(node, 'ifconfig')

BaseTestInternals = test_uuid.BaseTestInternals()
test_ifconfig_getnode()
