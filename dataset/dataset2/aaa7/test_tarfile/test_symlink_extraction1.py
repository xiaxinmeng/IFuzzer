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

@unittest.skipIf(hasattr(os, 'symlink'), 'Skip emulation if symlink exists')
def test_symlink_extraction1():
    LinkEmulationTest._test_link_extraction('ustar/symtype')

LinkEmulationTest = test_tarfile.LinkEmulationTest()
test_symlink_extraction1()
