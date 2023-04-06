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

def test_uuid5():
    equal = BaseTestUUID.assertEqual
    for (u, v) in [(BaseTestUUID.uuid.uuid5(BaseTestUUID.uuid.NAMESPACE_DNS, 'python.org'), '886313e1-3b8a-5372-9b90-0c9aee199e5d'), (BaseTestUUID.uuid.uuid5(BaseTestUUID.uuid.NAMESPACE_URL, 'http://python.org/'), '4c565f0d-3f5a-5890-b41b-20cf47701c5e'), (BaseTestUUID.uuid.uuid5(BaseTestUUID.uuid.NAMESPACE_OID, '1.3.6.1'), '1447fa61-5277-5fef-a9b3-fbc6e44f4af3'), (BaseTestUUID.uuid.uuid5(BaseTestUUID.uuid.NAMESPACE_X500, 'c=ca'), 'cc957dd1-a972-5349-98cd-874190002798')]:
        equal(u.variant, BaseTestUUID.uuid.RFC_4122)
        equal(u.version, 5)
        equal(u, BaseTestUUID.uuid.UUID(v))
        equal(str(u), v)

BaseTestUUID = test_uuid.BaseTestUUID()
test_uuid5()
