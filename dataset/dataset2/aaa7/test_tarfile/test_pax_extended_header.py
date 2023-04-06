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

def test_pax_extended_header():
    pax_headers = {'path': 'foo', 'uid': '123'}
    tar = tarfile.open(test_tarfile.tmpname, 'w', format=tarfile.PAX_FORMAT, encoding='iso8859-1')
    try:
        t = tarfile.TarInfo()
        t.name = 'äöü'
        t.uid = 8 ** 8
        t.pax_headers = pax_headers
        tar.addfile(t)
    finally:
        tar.close()
    tar = tarfile.open(test_tarfile.tmpname, encoding='iso8859-1')
    try:
        t = tar.getmembers()[0]
        PaxWriteTest.assertEqual(t.pax_headers, pax_headers)
        PaxWriteTest.assertEqual(t.name, 'foo')
        PaxWriteTest.assertEqual(t.uid, 123)
    finally:
        tar.close()

PaxWriteTest = test_tarfile.PaxWriteTest()
test_pax_extended_header()
