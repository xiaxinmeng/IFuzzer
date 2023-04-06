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
def test_legacy_block_size_warnings():

    class MockCrazyHash(object):
        """Ain't no block_size attribute here."""

        def __init__(TestVectorsTestCase, *args):
            TestVectorsTestCase._x = hashlib.sha256(*args)
            TestVectorsTestCase.digest_size = TestVectorsTestCase._x.digest_size

        def update(TestVectorsTestCase, v):
            TestVectorsTestCase._x.update(v)

        def digest(TestVectorsTestCase):
            return TestVectorsTestCase._x.digest()
    with warnings.catch_warnings():
        warnings.simplefilter('error', RuntimeWarning)
        with TestVectorsTestCase.assertRaises(RuntimeWarning):
            hmac.HMAC(b'a', b'b', digestmod=MockCrazyHash)
            TestVectorsTestCase.fail('Expected warning about missing block_size')
        MockCrazyHash.block_size = 1
        with TestVectorsTestCase.assertRaises(RuntimeWarning):
            hmac.HMAC(b'a', b'b', digestmod=MockCrazyHash)
            TestVectorsTestCase.fail('Expected warning about small block_size')

TestVectorsTestCase = test_hmac.TestVectorsTestCase()
test_legacy_block_size_warnings()
