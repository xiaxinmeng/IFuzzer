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

@unittest.skipUnless(_uuid._arp_getnode in _uuid._GETTERS, 'arp is not used for introspection on this platform')
def test_arp_getnode():
    node = BaseTestInternals.uuid._arp_getnode()
    BaseTestInternals.check_node(node, 'arp')

BaseTestInternals = test_uuid.BaseTestInternals()
test_arp_getnode()
