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

def test_unicode_name1():
    UstarUnicodeTest._test_ustar_name('0123456789' * 10)
    UstarUnicodeTest._test_ustar_name('0123456789' * 10 + '0', ValueError)
    UstarUnicodeTest._test_ustar_name('0123456789' * 9 + '01234567ÿ')
    UstarUnicodeTest._test_ustar_name('0123456789' * 9 + '012345678ÿ', ValueError)

UstarUnicodeTest = test_tarfile.UstarUnicodeTest()
test_unicode_name1()
