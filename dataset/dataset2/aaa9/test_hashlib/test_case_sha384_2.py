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

def test_case_sha384_2():
    HashLibTestCase.check('sha384', b'abcdefghbcdefghicdefghijdefghijkefghijklfghijklmghijklmn' + b'hijklmnoijklmnopjklmnopqklmnopqrlmnopqrsmnopqrstnopqrstu', '09330c33f71147e83d192fc782cd1b4753111b173b3b05d22fa08086e3b0f712' + 'fcc7c71a557e2db966c3e9fa91746039')

HashLibTestCase = test_hashlib.HashLibTestCase()
test_case_sha384_2()
