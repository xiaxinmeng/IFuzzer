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

def test_uuid3():
    equal = BaseTestUUID.assertEqual
    for (u, v) in [(BaseTestUUID.uuid.uuid3(BaseTestUUID.uuid.NAMESPACE_DNS, 'python.org'), '6fa459ea-ee8a-3ca4-894e-db77e160355e'), (BaseTestUUID.uuid.uuid3(BaseTestUUID.uuid.NAMESPACE_URL, 'http://python.org/'), '9fe8e8c4-aaa8-32a9-a55c-4535a88b748d'), (BaseTestUUID.uuid.uuid3(BaseTestUUID.uuid.NAMESPACE_OID, '1.3.6.1'), 'dd1a1cef-13d5-368a-ad82-eca71acd4cd1'), (BaseTestUUID.uuid.uuid3(BaseTestUUID.uuid.NAMESPACE_X500, 'c=ca'), '658d3002-db6b-3040-a1d1-8ddd7d189a4d')]:
        equal(u.variant, BaseTestUUID.uuid.RFC_4122)
        equal(u.version, 3)
        equal(u, BaseTestUUID.uuid.UUID(v))
        equal(str(u), v)

BaseTestUUID = test_uuid.BaseTestUUID()
test_uuid3()
