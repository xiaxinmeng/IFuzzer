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

def test_unicode_longname2():
    UstarUnicodeTest._test_ustar_name('0123456789' * 15 + '01ÿ/2' + '0123456789' * 10, ValueError)
    UstarUnicodeTest._test_ustar_name('0123456789' * 15 + '01ÿÿ/' + '0123456789' * 10, ValueError)

UstarUnicodeTest = test_tarfile.UstarUnicodeTest()
test_unicode_longname2()
