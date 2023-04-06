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

@unittest.skipUnless(os.name == 'nt', 'requires Windows')
def test_windll_getnode():
    node = TestInternalsWithExtModule.uuid._windll_getnode()
    TestInternalsWithExtModule.check_node(node)

TestInternalsWithExtModule = test_uuid.TestInternalsWithExtModule()
test_windll_getnode()
