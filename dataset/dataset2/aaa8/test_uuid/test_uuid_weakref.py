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

def test_uuid_weakref():
    strong = BaseTestUUID.uuid.uuid4()
    weak = weakref.ref(strong)
    BaseTestUUID.assertIs(strong, weak())

BaseTestUUID = test_uuid.BaseTestUUID()
test_uuid_weakref()
