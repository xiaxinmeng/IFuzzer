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

def test_hmac_compare_digest():
    CompareDigestTestCase._test_compare_digest(hmac.compare_digest)
    if openssl_compare_digest is not None:
        CompareDigestTestCase.assertIs(hmac.compare_digest, openssl_compare_digest)
    else:
        CompareDigestTestCase.assertIs(hmac.compare_digest, operator_compare_digest)

CompareDigestTestCase = test_hmac.CompareDigestTestCase()
test_hmac_compare_digest()
