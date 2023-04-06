import binascii
import functools
import hmac
import hashlib
import unittest
import unittest.mock
import warnings
from test.support import hashlib_helper
from _operator import _compare_digest as operator_compare_digest
from _hashlib import HMAC as C_HMAC
from _hashlib import hmac_new as c_hmac_new
from _hashlib import compare_digest as openssl_compare_digest
import test_hmac

@hashlib_helper.requires_hashdigest('sha256')
def test_equality():
    h1 = hmac.HMAC(b'key', digestmod='sha256')
    h1.update(b'some random text')
    h2 = h1.copy()
    CopyTestCase.assertEqual(h1.digest(), h2.digest(), "Digest of copy doesn't match original digest.")
    CopyTestCase.assertEqual(h1.hexdigest(), h2.hexdigest(), "Hexdigest of copy doesn't match original hexdigest.")

CopyTestCase = test_hmac.CopyTestCase()
test_equality()
