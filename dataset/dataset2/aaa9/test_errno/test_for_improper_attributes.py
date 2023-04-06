import errno
import unittest
import test_errno
std_c_errors = frozenset(['EDOM', 'ERANGE'])
def test_for_improper_attributes():
    for error_code in std_c_errors:
        ErrnoAttributeTests.assertTrue(hasattr(errno, error_code), 'errno is missing %s' % error_code)

ErrnoAttributeTests = test_errno.ErrnoAttributeTests()
test_for_improper_attributes()
