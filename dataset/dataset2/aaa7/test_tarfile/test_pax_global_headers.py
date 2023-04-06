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

def test_pax_global_headers():
    tar = tarfile.open(test_tarfile.tarname, encoding='iso8859-1')
    try:
        tarinfo = tar.getmember('pax/regtype1')
        PaxReadTest.assertEqual(tarinfo.uname, 'foo')
        PaxReadTest.assertEqual(tarinfo.gname, 'bar')
        PaxReadTest.assertEqual(tarinfo.pax_headers.get('VENDOR.umlauts'), 'ÄÖÜäöüß')
        tarinfo = tar.getmember('pax/regtype2')
        PaxReadTest.assertEqual(tarinfo.uname, '')
        PaxReadTest.assertEqual(tarinfo.gname, 'bar')
        PaxReadTest.assertEqual(tarinfo.pax_headers.get('VENDOR.umlauts'), 'ÄÖÜäöüß')
        tarinfo = tar.getmember('pax/regtype3')
        PaxReadTest.assertEqual(tarinfo.uname, 'tarfile')
        PaxReadTest.assertEqual(tarinfo.gname, 'tarfile')
        PaxReadTest.assertEqual(tarinfo.pax_headers.get('VENDOR.umlauts'), 'ÄÖÜäöüß')
    finally:
        tar.close()

PaxReadTest = test_tarfile.PaxReadTest()
test_pax_global_headers()
