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

def test_iso8859_1_filename():
    UnicodeTest._test_unicode_filename('iso8859-1')

UnicodeTest = test_tarfile.UnicodeTest()

test_iso8859_1_filename()
