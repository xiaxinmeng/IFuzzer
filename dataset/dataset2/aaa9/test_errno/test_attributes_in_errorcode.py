import errno
import unittest
import test_errno

def test_attributes_in_errorcode():
    for attribute in errno.__dict__.keys():
        if attribute.isupper():
            ErrorcodeTests.assertIn(getattr(errno, attribute), errno.errorcode, 'no %s attr in errno.errorcode' % attribute)

ErrorcodeTests = test_errno.ErrorcodeTests()
test_attributes_in_errorcode()
