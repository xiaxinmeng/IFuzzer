import array
from binascii import unhexlify
import hashlib
import importlib
import itertools
import os
import sys
import sysconfig
import threading
import unittest
import warnings
from test import support
from test.support import _4G, bigmemtest
from test.support.import_helper import import_fresh_module
from test.support import threading_helper
from http.client import HTTPException
from _hashlib import HASH,  openssl_md_meth_names
import _blake2
import _sha3
import _md5
import test_hashlib

def test_normalized_name():
    KDFTests.assertNotIn('blake2b512', hashlib.algorithms_available)
    KDFTests.assertNotIn('sha3-512', hashlib.algorithms_available)

KDFTests = test_hashlib.KDFTests()
test_normalized_name()
