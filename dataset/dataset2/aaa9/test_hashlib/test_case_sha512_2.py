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

def test_case_sha512_2():
    HashLibTestCase.check('sha512', b'abcdefghbcdefghicdefghijdefghijkefghijklfghijklmghijklmn' + b'hijklmnoijklmnopjklmnopqklmnopqrlmnopqrsmnopqrstnopqrstu', '8e959b75dae313da8cf4f72814fc143f8f7779c6eb9f7fa17299aeadb6889018' + '501d289e4900f7e4331b99dec4b5433ac7d329eeb6dd26545e96e55b874be909')

HashLibTestCase = test_hashlib.HashLibTestCase()
test_case_sha512_2()
