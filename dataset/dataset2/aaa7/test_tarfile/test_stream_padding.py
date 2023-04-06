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

def test_stream_padding():
    tar = tarfile.open(test_tarfile.tmpname, StreamWriteTest.mode)
    tar.close()
    if StreamWriteTest.decompressor:
        dec = StreamWriteTest.decompressor()
        with open(test_tarfile.tmpname, 'rb') as fobj:
            data = fobj.read()
        data = dec.decompress(data)
        StreamWriteTest.assertFalse(dec.unused_data, 'found trailing data')
    else:
        with StreamWriteTest.open(test_tarfile.tmpname) as fobj:
            data = fobj.read()
    StreamWriteTest.assertEqual(data.count(b'\x00'), tarfile.RECORDSIZE, 'incorrect zero padding')

StreamWriteTest = test_tarfile.StreamWriteTest()
test_stream_padding()
