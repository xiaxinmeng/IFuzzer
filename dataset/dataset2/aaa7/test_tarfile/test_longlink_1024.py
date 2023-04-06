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

def test_longlink_1024():
    GNUWriteTest._test('name', 'longlnk/' * 127 + 'longlink')

GNUWriteTest = test_tarfile.GNUWriteTest()
test_longlink_1024()
