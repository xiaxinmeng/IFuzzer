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

def test_parse_mac():
    BaseTestInternals.check_parse_mac(False)

BaseTestInternals = test_uuid.BaseTestInternals()
test_parse_mac()
