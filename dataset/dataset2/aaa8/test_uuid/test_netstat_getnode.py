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

@unittest.skipUnless(_uuid._netstat_getnode in _uuid._GETTERS, 'netstat is not used for introspection on this platform')
def test_netstat_getnode():
    node = BaseTestInternals.uuid._netstat_getnode()
    BaseTestInternals.check_node(node, 'netstat')

BaseTestInternals = test_uuid.BaseTestInternals()
test_netstat_getnode()
