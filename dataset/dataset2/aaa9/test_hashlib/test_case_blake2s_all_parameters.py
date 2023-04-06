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
from _hashlib import HASH, openssl_md_meth_names
import _blake2
import _sha3
import _md5
import test_hashlib

@test_hashlib.requires_blake2
def test_case_blake2s_all_parameters():
    HashLibTestCase.check('blake2s', b'foo', 'bf2a8f7fe3c555012a6f8046e646bc75', digest_size=16, key=b'bar', salt=b'baz', person=b'bing', fanout=2, depth=3, leaf_size=4, node_offset=5, node_depth=6, inner_size=7, last_node=True)

HashLibTestCase = test_hashlib.HashLibTestCase()
test_case_blake2s_all_parameters()
