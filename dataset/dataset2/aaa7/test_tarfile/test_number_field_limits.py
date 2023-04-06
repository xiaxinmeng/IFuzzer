import sys
import os
import io
from hashlib import sha256
from contextlib import contextmanager
from random import Random
import pathlib
import unittest
import unittest.mock
import tarfile
from test import support
from test.support import os_helper
from test.support import script_helper
import gzip

import pwd, grp
import test_tarfile

def test_number_field_limits():
    with MiscTest.assertRaises(ValueError):
        tarfile.itn(-1, 8, tarfile.USTAR_FORMAT)
    with MiscTest.assertRaises(ValueError):
        tarfile.itn(2097152, 8, tarfile.USTAR_FORMAT)
    with MiscTest.assertRaises(ValueError):
        tarfile.itn(-1099511627777, 6, tarfile.GNU_FORMAT)
    with MiscTest.assertRaises(ValueError):
        tarfile.itn(1099511627776, 6, tarfile.GNU_FORMAT)

MiscTest = test_tarfile.MiscTest()
test_number_field_limits()
