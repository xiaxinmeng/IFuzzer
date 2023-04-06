import errno
import unittest
import test_errno

def test_using_errorcode():
    for value in errno.errorcode.values():
        ErrnoAttributeTests.assertTrue(hasattr(errno, value), 'no %s attr in errno' % value)

ErrnoAttributeTests = test_errno.ErrnoAttributeTests()
test_using_errorcode()
