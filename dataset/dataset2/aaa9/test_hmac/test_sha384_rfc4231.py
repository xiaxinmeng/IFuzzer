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

@hashlib_helper.requires_hashdigest('sha384', openssl=True)
def test_sha384_rfc4231():
    TestVectorsTestCase._rfc4231_test_cases(hashlib.sha384, 'sha384', 48, 128)

TestVectorsTestCase = test_hmac.TestVectorsTestCase()
test_sha384_rfc4231()
